# NetScope — Local Network Service Reporter

> A beginner-friendly defensive network scanning and reporting application built with **Python, Flask, Nmap, and SQLite**.

**Author:** Tamil Vanan J

---

## 📌 Project Overview

**NetScope** is a local network service reporting tool designed for **defensive security learning and authorized network assessment**.

The application uses **Nmap** to scan an authorized target, identifies accessible network services, stores scan history in **SQLite**, and presents the results through a simple **Flask web interface**.

It also provides multiple report formats and defensive recommendations based on the discovered services.

---

## ✨ Features

- 🔎 **Local / Private Network Scanning**
- 🌐 **Nmap-based Port and Service Detection**
- 📋 **Open Port and Service Reporting**
- 🧩 **Service and Version Information**
- 💾 **SQLite Scan History**
- 📊 **Previous Scan Review**
- 📝 **HTML Report Generation**
- 📄 **PDF Report Generation**
- 🗂️ **XML Report Generation**
- 📧 **Email Report Support**
- 🛡️ **Defensive Security Recommendations**
- 🧪 **Scanner Testing**
- 🎨 **Simple Flask Web Interface**
- ✅ **Target Validation for Safer Use**

---

## 🏗️ Project Structure

```text
NetScope_Tamil_Vanan_J/
│
├── app.py                  # Main Flask application
├── database.py             # SQLite database and scan history
├── email_report.py         # Email report functionality
├── pdf_report.py           # PDF report generation
├── recommendations.py      # Defensive recommendations
├── scanner_test.py         # Scanner-related tests
├── xml_report.py           # XML report generation
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignored files
│
├── scanner/
│   └── ...                 # Nmap scanning components
│
├── templates/
│   └── ...                 # Flask HTML templates
│
├── static/
│   └── ...                 # CSS / static assets
│
├── reports/
│   └── ...                 # Generated reports
│
└── docs/
    └── screenshots/        # Project screenshots
```

---

## ⚙️ Requirements

Before running NetScope, install:

- **Python 3**
- **Nmap**
- **pip**
- A modern web browser

Python dependencies are listed in:

```text
requirements.txt
```

Current project requirements include:

```text
Flask>=3.0,<4.0
python-nmap>=0.7.1
```

> **Note:** Nmap itself must be installed separately on the operating system.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J.git
cd NetScope-Tamil-Vanan-J
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Nmap

Install Nmap separately and make sure it is available to the system.

You can verify the installation with:

```bash
nmap --version
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

The application provides a web interface for entering an authorized target and viewing scan results.

---

## 🔍 Scanning Workflow

```text
Authorized Target
       │
       ▼
   Target Validation
       │
       ▼
    Nmap Scan
       │
       ▼
Open Ports & Services
       │
       ├───────────────┐
       ▼               ▼
  SQLite History   Recommendations
       │
       ▼
 Generate Reports
       │
   ┌───┼────┐
   ▼   ▼    ▼
 HTML PDF  XML
       │
       ▼
   Email Report
```

---

## 📊 Scan Results

NetScope displays information such as:

| Field | Description |
|---|---|
| Port | Detected network port |
| Protocol | TCP/UDP protocol |
| Service | Service identified by Nmap |
| Version | Detected service/version information |

Example services may include HTTP, Microsoft-DS, MSRPC, and other services detected by Nmap.

> Results depend on the target system and the services that are accessible during the scan.

---

## 🛡️ Defensive Recommendations

NetScope provides recommendations intended to help users review exposed services.

Examples include:

- Review each exposed service.
- Disable services that are not required.
- Keep operating systems and network services patched.
- Review detected service versions.
- Restrict unnecessary network exposure.
- Perform scans only on systems you are authorized to assess.

---

## 📝 Reporting

NetScope supports multiple reporting options:

### HTML Report

A browser-friendly report containing scan information and defensive recommendations.

### PDF Report

A portable document version of the scan results.

### XML Report

Structured scan information suitable for further processing.

### Email Report

Allows generated report information to be sent through an appropriately configured email system.

---

## 💾 Database

NetScope uses **SQLite** to store scan history.

The database allows users to:

- Store previous scan results
- Review earlier scans
- Maintain local scan history

The database is created locally when the application is executed.

---

## 🧪 Testing

The project includes:

```text
scanner_test.py
```

This file is used to test scanner-related functionality and helps verify that scanning components behave as expected.

Run the test file with:

```bash
python scanner_test.py
```

---

## 🔐 Security & Responsible Use

NetScope is designed for **defensive and educational purposes**.

### Only scan:

- Your own computer
- Your own local network
- Private systems you are authorized to test
- Systems where you have explicit permission

### Do not:

- Scan public systems without authorization
- Scan networks that you do not own or have permission to assess
- Use the application for unauthorized security testing

Nmap must be installed separately, and scan results depend on the services available on the target.

---

## ⚠️ Limitations

- Nmap must be installed separately.
- Scan results depend on the target's accessible services.
- Service/version detection depends on what Nmap can identify.
- The Flask development server is intended for local/educational use, not production deployment.
- Email reporting requires appropriate email configuration.
- Report generation depends on the corresponding Python modules and installed dependencies.

---

## 📸 Screenshots

Project screenshots are available in:

```text
docs/screenshots/
```

These demonstrate the application's interface and scan/report workflow.

---

## 🎓 Educational Purpose

This project demonstrates practical concepts including:

- Python programming
- Flask web development
- Network scanning
- Nmap integration
- SQLite database management
- Report generation
- Basic defensive security concepts
- Automated testing
- Responsible security practices

---

## 📄 License

This project is intended for educational and authorized security-testing purposes.

---

## 👨‍💻 Author

**Tamil Vanan J**

GitHub:  
https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J
