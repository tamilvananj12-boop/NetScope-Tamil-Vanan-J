from datetime import datetime
from pathlib import Path
from time import perf_counter
from flask import Flask,flash,redirect,render_template,request,send_from_directory,url_for
from database import init_db,list_scans,save_scan
from scanner.nmap_scanner import run_service_scan
from scanner.validator import is_allowed_target
app=Flask(__name__); app.secret_key="netscope-local-demo-key"
REPORT_DIR=Path("reports"); REPORT_DIR.mkdir(exist_ok=True)
def recommendations(services):
    tips=[]; names={x["name"].lower() for x in services}
    tips.append("Review each exposed service and disable services that are not required." if services else "No open services were reported by the scan.")
    if "telnet" in names: tips.append("Replace Telnet with a secure remote-management method where possible.")
    if "ftp" in names: tips.append("Review FTP usage and prefer encrypted file-transfer methods.")
    if any(x["port"] in {22,3389} for x in services): tips.append("Restrict remote-administration services to trusted systems.")
    tips.append("Keep operating systems and network services patched and updated."); return tips
def create_report(target,result,duration,tips,filename):
    rows=[]
    for x in result["services"]:
        version=(f'{x["product"]} {x["version"]}').strip() or "Not reported"
        rows.append("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(x["port"],x["protocol"],x["name"],version))
    html="""<!doctype html><html><head><meta charset="utf-8"><title>NetScope Report</title><style>body{font-family:Arial;max-width:900px;margin:40px auto;padding:0 20px}table{width:100%;border-collapse:collapse}th,td{padding:10px;border:1px solid #ddd;text-align:left}th{background:#eee}</style></head><body><h1>NetScope Service Report</h1><p><b>Target:</b> __TARGET__</p><p><b>Generated:</b> __DATE__</p><p><b>Duration:</b> __DURATION__ seconds</p><p><b>Services:</b> __COUNT__</p><h2>Discovered Services</h2><table><tr><th>Port</th><th>Protocol</th><th>Service</th><th>Version/Product</th></tr>__TABLE__</table><h2>Defensive Recommendations</h2><ul>__NOTES__</ul></body></html>"""
    html=html.replace("__TARGET__",target).replace("__DATE__",datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace("__DURATION__",f"{duration:.2f}").replace("__COUNT__",str(len(result["services"]))).replace("__TABLE__","".join(rows) or '<tr><td colspan="4">No open services reported.</td></tr>').replace("__NOTES__","".join("<li>"+x+"</li>" for x in tips))
    (REPORT_DIR/filename).write_text(html,encoding="utf-8")
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        target=request.form.get("target","").strip()
        if not is_allowed_target(target): flash("Enter localhost or a private/local target you are authorized to test."); return redirect(url_for("index"))
        started=perf_counter()
        try: result=run_service_scan(target)
        except Exception as error: flash(f"Scan failed: {error}"); return redirect(url_for("index"))
        duration=perf_counter()-started; tips=recommendations(result["services"]); filename=f"netscope_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        create_report(target,result,duration,tips,filename); save_scan(target,datetime.now().isoformat(timespec="seconds"),duration,len(result["services"]),filename)
        return render_template("results.html",target=target,result=result,duration=duration,tips=tips,report_file=filename)
    return render_template("index.html")
@app.route("/history")
def history(): return render_template("history.html",scans=list_scans())
@app.route("/reports/<path:filename>")
def reports(filename): return send_from_directory(REPORT_DIR,filename,as_attachment=True)
if __name__=="__main__": init_db(); app.run(debug=True)
