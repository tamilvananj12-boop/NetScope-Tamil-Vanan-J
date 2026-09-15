from datetime import datetime
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
from scanner.nmap_scanner import run_service_scan
from scanner.validator import is_allowed_target


app = Flask(__name__)
app.secret_key = "netscope-local-demo-key"

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)


def recommendations(services):
    """Generate defensive recommendations from discovered services."""
    tips = []
    names = {service["name"].lower() for service in services}

    if services:
        tips.append(
            "Review each exposed service and disable services that are not required."
        )
    else:
        tips.append("No open services were reported by the scan.")

    if "telnet" in names:
        tips.append(
            "Replace Telnet with a secure remote-management method where possible."
        )

    if "ftp" in names:
        tips.append(
            "Review FTP usage and prefer encrypted file-transfer methods."
        )

    if any(service["port"] in {22, 3389} for service in services):
        tips.append(
            "Restrict remote-administration services to trusted systems."
        )

    tips.append(
        "Keep operating systems and network services patched and updated."
    )

    return tips


def create_report(target, result, duration, tips, filename):
    """Create a standalone HTML report for a completed scan."""
    rows = []

    for service in result["services"]:
        version = (
            f'{service["product"]} {service["version"]}'
        ).strip() or "Not reported"

        rows.append(
            "<tr>"
            f'<td>{service["port"]}</td>'
            f'<td>{service["protocol"]}</td>'
            f'<td>{service["name"]}</td>'
            f"<td>{version}</td>"
            "</tr>"
        )

    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NetScope Report</title>
<style>
body {
    font-family: Arial, sans-serif;
    max-width: 960px;
    margin: 40px auto;
    padding: 0 20px;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}
th, td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
}
th {
    background: #f2f2f2;
}
li {
    margin: 8px 0;
}
</style>
</head>
<body>
<h1>NetScope — Local Network Service Report</h1>
<p><strong>Target:</strong> __TARGET__</p>
<p><strong>Generated:</strong> __DATE__</p>
<p><strong>Duration:</strong> __DURATION__ seconds</p>
<p><strong>Services found:</strong> __COUNT__</p>

<h2>Discovered Services</h2>
<table>
<thead>
<tr>
<th>Port</th>
<th>Protocol</th>
<th>Service</th>
<th>Version</th>
</tr>
</thead>
<tbody>
__TABLE__
</tbody>
</table>

<h2>Defensive Recommendations</h2>
<ul>
__NOTES__
</ul>
</body>
</html>
"""

    notes = "".join(f"<li>{tip}</li>" for tip in tips)

    html = html.replace("__TARGET__", target)
    html = html.replace(
        "__DATE__",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    html = html.replace("__DURATION__", f"{duration:.2f}")
    html = html.replace(
        "__COUNT__",
        str(len(result["services"])),
    )
    html = html.replace("__TABLE__", "".join(rows))
    html = html.replace("__NOTES__", notes)

    (REPORT_DIR / filename).write_text(
        html,
        encoding="utf-8",
    )


@app.route("/", methods=["GET", "POST"])
def index():
    """Display the scan form and process scan requests."""
    if request.method == "POST":
        target = request.form.get("target", "").strip()

        if not is_allowed_target(target):
            flash(
                "Enter localhost or a private/local target "
                "you are authorized to test."
            )
            return redirect(url_for("index"))

        started = perf_counter()

        try:
            result = run_service_scan(target)
        except Exception as error:
            flash(f"Scan failed: {error}")
            return redirect(url_for("index"))

        duration = perf_counter() - started
        tips = recommendations(result["services"])

        filename = (
            f'netscope_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
        )

        create_report(
            target,
            result,
            duration,
            tips,
            filename,
        )

        save_scan(
            target,
            datetime.now().isoformat(timespec="seconds"),
            duration,
            len(result["services"]),
            filename,
        )

        return render_template(
            "results.html",
            target=target,
            result=result,
            duration=duration,
            tips=tips,
            report_file=filename,
        )

    return render_template("index.html")


@app.route("/history")
def history():
    """Display previous scan history."""
    return render_template(
        "history.html",
        scans=list_scans(),
    )


@app.route("/reports/<path:filename>")
def reports(filename):
    """Serve generated HTML reports."""
    return send_from_directory(
        REPORT_DIR,
        filename,
        as_attachment=True,
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)