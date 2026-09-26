# NetScope — Local Network Service Reporter

> A beginner-friendly defensive network scanning and reporting application built with **Python, Flask, Nmap, and SQLite**.

**Author:** Tamil Vanan J

---

## 📌 Project Overview

**NetScope** is a local network service reporting tool designed for **defensive security learning and authorized network assessment**.

The application uses **Nmap** to scan an authorized local/private target, identify TCP and UDP services, collect service/version information, attempt OS detection, store scan history in **SQLite**, and present results through a Flask web interface.

It also generates **HTML, PDF, and XML reports** and provides defensive recommendations.

---

## ✨ Features

- 🔎 Local / private network target validation
- 🌐 Nmap-based port scanning
- 🔵 TCP port scanning
- 🟣 UDP port scanning
- 🧩 Service detection
- 🏷️ Service/version detection
- 💻 Operating-system detection when supported by Nmap/permissions
- 💾 SQLite scan history
- 📊 Previous scan review
- 📝 HTML report generation
- 📄 PDF report generation
- 🗂️ XML report generation
- 📧 Email report support module
- 🛡️ Defensive security recommendations
- 🧪 Scanner tests
- 🎨 Flask web interface
- ⬇️ HTML/PDF/XML report download buttons

---

## 🏗️ Project Structure

```text
NetScope_Tamil_Vanan_J/
│
├── app.py                  # Main Flask application and report workflow
├── database.py             # SQLite database and scan history
├── email_report.py         # Email report functionality
├── pdf_report.py           # PDF report generation
├── recommendations.py      # Defensive recommendations
├── scanner_test.py         # Scanner tests
├── xml_report.py           # XML report generation
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignored files
│
├── scanner/
│   ├── __init__.py
│   ├── nmap_scanner.py     # TCP/UDP/service/version/OS scanning
│   └── validator.py        # Local/private target validation
│
├── templates/              # Flask HTML templates
├── static/                 # CSS/static assets
├── reports/                # Generated HTML/PDF/XML reports
│
└── docs/
    └── screenshots/        # Project screenshots
```

---

## ⚙️ Requirements

Install:

- **Python 3**
- **Nmap**
- **pip**
- A modern web browser

Python packages are listed in `requirements.txt`:

```text
Flask>=3.0,<4.0
python-nmap>=0.7.1
reportlab>=4.0,<5.0
```

> **Important:** Nmap is a separate system application. Install it separately and make sure `nmap --version` works in the terminal.

---

## 🚀 Installation

```bash
git clone https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J.git
cd NetScope-Tamil-Vanan-J

python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt
nmap --version
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

Enter **localhost or a private/local system you are authorized to test**.

---

## 🔍 Scanning Workflow

```text
Authorized Local Target
        │
        ▼
 Target Validation
        │
        ▼
     Nmap Scan
   ┌────┼───────────────┐
   ▼    ▼       ▼       ▼
  TCP  UDP   Service   OS
        │    Version   Detection
        └────┬──────────┘
             ▼
       Scan Results
             │
     ┌───────┼────────┐
     ▼       ▼        ▼
   SQLite  Reports  Recommendations
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
      HTML  PDF    XML
```

---

## 📊 Scan Results

| Field | Description |
|---|---|
| Port | Detected network port |
| Protocol | TCP or UDP |
| State | Port/service state |
| Service | Service identified by Nmap |
| Version | Product/version information |
| OS | Best OS match reported by Nmap |

Results depend on the target, Nmap capabilities, and permissions available to the scan.

---

## 📝 Reporting

### HTML Report
Browser-friendly report containing host/OS information, TCP/UDP ports, services, versions, and recommendations.

### PDF Report
Portable document containing the scan results and defensive recommendations.

### XML Report
Structured report containing host information and detailed port/service data.

The results page provides direct **Download HTML Report**, **Download PDF Report**, and **Download XML Report** buttons.

---

## 💾 Database

NetScope uses **SQLite** to store local scan history.

The database stores the target, scan time, duration, number of detected services, and generated HTML report filename.

---

## 🧪 Testing

Run:

```bash
python scanner_test.py
```

The tests cover basic scan data, TCP/UDP protocol handling, and OS-result parsing.

---

## 🔐 Security & Responsible Use

NetScope is designed for **defensive and educational purposes**.

Only scan:

- Your own computer
- Your own local network
- Private systems you are authorized to test
- Systems where you have explicit permission

Do not use the application to scan public systems or networks without authorization.

---

## ⚠️ Limitations

- Nmap must be installed separately.
- UDP and OS detection can require elevated privileges depending on the operating system.
- If privileged Nmap features fail, NetScope falls back to a TCP service scan so the application can still run.
- Scan results depend on services accessible on the target.
- Service/version detection depends on what Nmap can identify.
- The Flask development server is intended for local/educational use, not production deployment.
- Email reporting requires appropriate SMTP configuration.

---

## 📸 Screenshots

Project screenshots are available in:

```text
docs/screenshots/
```

---

## 🎓 Educational Purpose

This project demonstrates:

- Python programming
- Flask web development
- TCP/UDP network scanning
- Nmap integration
- Service/version detection
- OS detection
- SQLite database management
- HTML/PDF/XML report generation
- Defensive security concepts
- Automated testing
- Responsible security practices

---

## 👨‍💻 Author

**Tamil Vanan J**

GitHub: https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J
