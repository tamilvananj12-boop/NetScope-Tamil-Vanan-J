# 🔎 NetScope — Local Network Service Reporter

> **A Python + Flask based local network service reporting tool powered by Nmap**

**Author:** Tamil Vanan J

**GitHub Repository:** https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J

---

## 📌 Project Overview

**NetScope** is a local network service reporting application developed using **Python, Flask, and Nmap**. It scans an authorized target, identifies accessible TCP and UDP services, collects service/version and operating-system information when available, and presents the results through a web interface.

The application also generates downloadable **HTML, PDF, and XML reports**, making the scan results easy to view, save, and process.

---

## ✨ Key Features

### 🔍 Network Scanning
- TCP port scanning using Nmap
- UDP port scanning
- Open and open|filtered port detection
- Service name detection
- Product detection
- Service/version detection
- Operating-system detection
- Hostname and target information

### 📊 Web-Based Results
- Clean Flask web interface
- Displays discovered ports and services
- Shows TCP/UDP protocol information
- Shows port state
- Shows service, product, and version details when available
- Displays operating-system information
- Provides defensive security recommendations

### 📄 Report Generation
NetScope provides three report formats:

- **HTML Report** — view the complete report in a browser
- **PDF Report** — download a formatted portable report
- **XML Report** — download structured scan data for further processing

### 🧪 Testing
- Scanner test support
- Basic validation of scanning/reporting functionality

---

## 🖥️ Example Scan Information

A scan can display information such as:

| Field | Example |
|---|---|
| Target | `127.0.0.1` |
| Hostname | `localhost` |
| Operating System | Microsoft Windows 11 |
| Port | `445` |
| Protocol | TCP |
| State | open |
| Service | microsoft-ds |
| Product | Microsoft Windows RPC |
| Version | When detected by Nmap |

The exact results depend on the target, network configuration, Nmap capabilities, and available permissions.

---

## 📥 Report Download Options

After completing a scan, the results page provides:

**Download HTML Report**  
Downloads the browser-friendly HTML version.

**Download PDF Report**  
Downloads a formatted PDF version generated using ReportLab.

**Download XML Report**  
Downloads structured XML data containing the scan information.

These reports are generated from the scan results and are stored in the project's `reports/` directory.

---

## 🔬 Nmap Integration

Nmap is the main scanning engine used by NetScope.

NetScope uses Nmap to perform network discovery and collect information about accessible services.

### Nmap Features Used

- TCP scanning
- UDP scanning
- Service detection
- Version detection
- OS detection
- Port-state detection

### ⚠️ Nmap Requirement

Nmap is a separate system application and must be installed independently from the Python packages.

After installation, make sure the `nmap` command is available through the system PATH.

Some UDP and OS detection techniques may require elevated privileges depending on the operating system and scan configuration.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core application and scanning logic |
| **Flask** | Web application framework |
| **Nmap** | Network and service scanning |
| **HTML / CSS** | Web interface and report presentation |
| **ReportLab** | PDF report generation |
| **XML** | Structured report generation |
| **Git / GitHub** | Version control and project hosting |

---

## 📁 Project Structure

```text
NetScope_Tamil_Vanan_J/
│
├── app.py                    # Flask application
├── database.py               # Database operations
├── email_report.py           # Email reporting functionality
├── pdf_report.py             # PDF report generation
├── recommendations.py        # Defensive recommendations
├── requirements.txt          # Python dependencies
├── scanner_test.py           # Scanner tests
├── xml_report.py             # XML report generation
│
├── scanner/
│   ├── __init__.py
│   └── nmap_scanner.py       # Nmap scanning logic
│
├── templates/
│   └── results.html          # Results web page
│
├── static/
│   └── ...                   # Static web assets
│
├── docs/
│   └── screenshots/          # Project screenshots
│
└── reports/
    └── ...                   # Generated HTML/PDF/XML reports
```

---

## ⚙️ Requirements

### Software Requirements

- Python 3.x
- Nmap
- Web browser
- Git (optional, for GitHub)

### Python Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the Python dependencies required by the application.

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J.git
```

### 2. Enter the Project Folder

```bash
cd NetScope-Tamil-Vanan-J
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Nmap

Install Nmap separately on the operating system and make sure it is available from the terminal.

Verify the installation:

```bash
nmap --version
```

### 5. Run NetScope

```bash
python app.py
```

### 6. Open the Web Application

Open the local Flask address displayed in the terminal, usually:

```text
http://127.0.0.1:5000
```

Then enter an authorized target and start the scan.

---

## 🔄 Application Workflow

```text
User
  │
  ▼
Flask Web Interface
  │
  ▼
Target IP / Hostname
  │
  ▼
Nmap Scanner
  │
  ├── TCP Scan
  ├── UDP Scan
  ├── Service Detection
  ├── Version Detection
  └── OS Detection
  │
  ▼
Scan Results
  │
  ├── Defensive Recommendations
  │
  ├── HTML Report
  ├── PDF Report
  └── XML Report
```

---

## 🧪 Testing

The project includes scanner testing support.

Run:

```bash
python scanner_test.py
```

Testing should be performed against systems and networks that you own or are explicitly authorized to test.

---

## 📸 Project Screenshots

Project screenshots are stored in:

```text
docs/screenshots/
```

Current screenshots demonstrate the application interface, scan results, and generated report functionality.

---

## 🛡️ Defensive Recommendations

NetScope can provide basic defensive recommendations based on discovered services.

Examples include:

- Review exposed services.
- Disable services that are not required.
- Keep operating systems and network services patched.
- Review unnecessary open ports.
- Investigate unexpected services.
- Restrict network access where appropriate.

These recommendations are informational and should be reviewed according to the actual system configuration.

---

## 🔐 Security & Responsible Use

NetScope is designed for **local, educational, and authorized security testing**.

Only scan:

- Systems you own
- Networks you administer
- Targets for which you have explicit permission

Do not use the application to scan unauthorized systems or networks.

---

## ⚠️ Limitations

- Nmap must be installed separately.
- UDP scanning may require elevated privileges.
- OS detection may require elevated privileges.
- Service/version information depends on what Nmap can identify.
- Results depend on network conditions and target configuration.
- Some services may not expose enough information for accurate version detection.
- PDF generation requires the ReportLab dependency.
- The Flask development server is intended for local/educational use and is not a production server.
- Email reporting requires appropriate SMTP configuration if that feature is used.

---

## 🎓 Educational Purpose

This project demonstrates practical concepts in:

- Python programming
- Flask web development
- Computer networking
- TCP and UDP protocols
- Port scanning
- Network service discovery
- Nmap integration
- Operating-system detection
- Service/version detection
- HTML report generation
- PDF report generation
- XML report generation
- Defensive security recommendations
- Basic software testing
- Git and GitHub project management

---

## 📌 Project Status

**Status:** Completed / Working

The implemented application supports network scanning, result presentation, and HTML/PDF/XML report downloads.

---

## 🔗 GitHub Repository

**NetScope — Local Network Service Reporter**

https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J

---

## 👨‍💻 Author

**Tamil Vanan J**

NetScope — Local Network Service Reporter

---

> **Note:** Use NetScope responsibly and only on systems you are authorized to scan.
