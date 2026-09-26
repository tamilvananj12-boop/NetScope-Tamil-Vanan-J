from datetime import datetime
from html import escape
from pathlib import Path
from time import perf_counter

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from database import init_db, list_scans, save_scan
from pdf_report import generate_pdf_report
from recommendations import get_recommendations
from scanner.nmap_scanner import run_service_scan
from scanner.validator import is_allowed_target
from xml_report import generate_xml_report


app = Flask(__name__)
app.secret_key = "netscope-local-demo-key"

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def recommendations(services):
    """Generate simple defensive recommendations for the web UI."""
    tips = []
    names = {service["name"].lower() for service in services}

    if services:
        tips.append("Review each exposed service and disable services that are not required.")
    else:
        tips.append("No open services were reported by the scan.")

    if "telnet" in names:
        tips.append("Replace Telnet with a secure remote-management method where possible.")
    if "ftp" in names:
        tips.append("Review FTP usage and prefer encrypted file-transfer methods.")
    if any(service["port"] in {22, 3389} for service in services):
        tips.append("Restrict remote-administration services to trusted systems.")

    tips.append("Keep operating systems and network services patched and updated.")
    return tips


def create_html_report(target, result, duration, tips, filename):
    """Create a standalone HTML report for a completed scan."""
    rows = []

    for service in result["services"]:
        version = " ".join(
            value for value in [
                service.get("product", ""),
                service.get("version", ""),
                service.get("extrainfo", ""),
            ] if value
        ).strip() or "Not reported"

        rows.append(
            "<tr>"
            f"<td>{escape(str(service['port']))}</td>"
            f"<td>{escape(str(service['protocol']))}</td>"
            f"<td>{escape(str(service['state']))}</td>"
            f"<td>{escape(str(service['name']))}</td>"
            f"<td>{escape(version)}</td>"
            "</tr>"
        )

    host_rows = []
    for host in result["hosts"]:
        host_rows.append(
            "<tr>"
            f"<td>{escape(str(host.get('address', '')))}</td>"
            f"<td>{escape(str(host.get('hostname', '')) or 'N/A')}</td>"
            f"<td>{escape(str(host.get('state', '')))}</td>"
            f"<td>{escape(str(host.get('os', 'Not detected')))}</td>"
            "</tr>"
        )

    notes = "".join(f"<li>{escape(tip)}</li>" for tip in tips)

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NetScope Report</title>
<style>
body{{font-family:Arial,sans-serif;max-width:1050px;margin:40px auto;padding:0 20px;line-height:1.5}}
table{{width:100%;border-collapse:collapse;margin:16px 0 28px}}
th,td{{border:1px solid #ccc;padding:8px;text-align:left}}
th{{background:#eef2f7}}
li{{margin:8px 0}}
</style>
</head>
<body>
<h1>NetScope — Local Network Service Report</h1>
<p><strong>Target:</strong> {escape(target)}</p>
<p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
<p><strong>Duration:</strong> {duration:.2f} seconds</p>
<p><strong>Scan method:</strong> {escape(result.get("scan_arguments", ""))}</p>

<h2>Host & OS Information</h2>
<table>
<thead><tr><th>Address</th><th>Hostname</th><th>State</th><th>Operating System</th></tr></thead>
<tbody>{''.join(host_rows) or '<tr><td colspan="4">No host information reported.</td></tr>'}</tbody>
</table>

<h2>Port, Protocol & Service Results</h2>
<table>
<thead><tr><th>Port</th><th>Protocol</th><th>State</th><th>Service</th><th>Version</th></tr></thead>
<tbody>{''.join(rows) or '<tr><td colspan="5">No open services reported.</td></tr>'}</tbody>
</table>

<h2>Defensive Recommendations</h2>
<ul>{notes}</ul>
</body>
</html>"""

    (REPORT_DIR / filename).write_text(html, encoding="utf-8")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("target", "").strip()

        if not is_allowed_target(target):
            flash("Enter localhost or a private/local target you are authorized to test.")
            return redirect(url_for("index"))

        started = perf_counter()

        try:
            result = run_service_scan(target)
        except Exception as error:
            flash(f"Scan failed: {error}")
            return redirect(url_for("index"))

        duration = perf_counter() - started
        tips = recommendations(result["services"])
        detailed_recommendations = get_recommendations(
            [service["port"] for service in result["services"]]
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        html_filename = f"netscope_{timestamp}.html"
        pdf_filename = f"netscope_{timestamp}.pdf"
        xml_filename = f"netscope_{timestamp}.xml"

        create_html_report(target, result, duration, tips, html_filename)

        generate_pdf_report(
            str(REPORT_DIR / pdf_filename),
            target,
            result["services"],
            detailed_recommendations,
            result["hosts"],
        )

        generate_xml_report(
            str(REPORT_DIR / xml_filename),
            target,
            result["services"],
            result["hosts"],
        )

        save_scan(
            target,
            datetime.now().isoformat(timespec="seconds"),
            duration,
            len(result["services"]),
            html_filename,
        )

        return render_template(
            "results.html",
            target=target,
            result=result,
            duration=duration,
            tips=tips,
            report_file=html_filename,
            pdf_report_file=pdf_filename,
            xml_report_file=xml_filename,
        )

    return render_template("index.html")


@app.route("/history")
def history():
    return render_template("history.html", scans=list_scans())


@app.route("/reports/<path:filename>")
def reports(filename):
    return send_from_directory(REPORT_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
