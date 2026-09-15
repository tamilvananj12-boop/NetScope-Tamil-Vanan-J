# NetScope — Local Network Service Reporter

**Author:** Tamil Vanan J

NetScope is a beginner-friendly Flask web application for discovering services running on local or private network systems. It uses **Nmap** for service discovery and provides a simple web interface for viewing scan results, defensive recommendations, scan history, and HTML reports.

> **Responsible Use:** Only scan localhost, private-network systems, or systems for which you have explicit permission. NetScope rejects public targets.

---

## Features

- 🔍 Local and private target validation
- 🌐 Nmap-based service discovery
- 📡 Open-port detection
- 🛠️ Service and version information
- ⏱️ Scan duration measurement
- 🛡️ Defensive security recommendations
- 🗄️ SQLite scan history
- 📄 HTML report generation
- 📋 Previous scan results can be viewed from the history page
- 💻 Simple and beginner-friendly Flask interface

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Web application framework |
| Nmap | Network service discovery |
| python-nmap | Python interface for Nmap |
| SQLite | Scan history database |
| HTML | Web page structure |
| CSS | User interface styling |
| Jinja2 | Flask template rendering |

---

## Requirements

Before running NetScope, install:

- Python 3.10 or newer
- Nmap
- Git (optional, for cloning the repository)

Nmap must be installed and available from the system terminal.

You can verify this with:

```powershell
nmap --version
```

---

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J.git
```

### 2. Open the project folder

```powershell
cd NetScope-Tamil-Vanan-J
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### 5. Install Python dependencies

```powershell
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application with:

```powershell
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open the address in a web browser.

---

## Usage

### Step 1 — Enter a Target

Enter a localhost or private-network target that you are authorized to scan.

Example:

```text
127.0.0.1
```

### Step 2 — Run the Scan

Click **Run Scan**.

NetScope uses Nmap to discover available network services on the target.

### Step 3 — View Results

The results page displays:

- Number of hosts
- Number of discovered services
- Scan duration
- Port numbers
- Protocols
- Service names
- Service/version information

### Step 4 — Review Recommendations

NetScope provides defensive recommendations based on the discovered services.

### Step 5 — View Scan History

Previous scans are stored in SQLite and can be viewed from the **History** page.

### Step 6 — Generate a Report

The application can generate an HTML report containing the scan results and defensive recommendations.

---

## Project Structure

```text
NetScope-Tamil-Vanan-J/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── scanner/
│   ├── __init__.py
│   ├── nmap_scanner.py
│   └── validator.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── results.html
│   └── history.html
│
├── static/
│   └── style.css
│
├── reports/
│   └── .gitkeep
│
└── docs/
    └── screenshots/
```

### File and Folder Description

| File / Folder | Description |
|---|---|
| `app.py` | Main Flask application and web routes |
| `database.py` | SQLite database operations and scan history |
| `requirements.txt` | Python package dependencies |
| `scanner/nmap_scanner.py` | Performs Nmap service scanning |
| `scanner/validator.py` | Validates allowed local/private targets |
| `templates/` | Flask HTML templates |
| `static/style.css` | Application styling |
| `reports/` | Stores generated reports locally |
| `docs/screenshots/` | Project screenshots for documentation |
| `.gitignore` | Prevents temporary and local files from being committed |

---

## Application Workflow

```text
User
  │
  ▼
Enter Local/Private Target
  │
  ▼
Target Validation
  │
  ├── Invalid ──► Reject Target
  │
  ▼
Nmap Service Scan
  │
  ▼
Process Scan Results
  │
  ├──► Display Services
  ├──► Generate Recommendations
  ├──► Save Scan History
  └──► Generate HTML Report
```

---

## Security and Responsible Use

NetScope is designed for **defensive and educational use**.

Only scan:

- Your own computer
- Your own local network
- Private systems you are authorized to test
- Systems where you have explicit permission

Do not use this application to scan public systems or networks without authorization.

NetScope includes target validation to prevent scanning of unauthorized public targets.

---

## Limitations

- Nmap must be installed separately on the system.
- Scan results depend on the services available on the target.
- The application is intended for local/educational use.
- The Flask development server should not be used as a production server.
- Service/version detection depends on what Nmap can identify.

---

## Future Improvements

Possible future improvements include:

- PDF report generation
- More detailed service analysis
- Improved dashboard visualizations
- Exporting scan history to CSV
- Additional security recommendations
- User authentication
- Background scanning for longer scans
- More detailed network reporting

---

## Screenshots

Screenshots of the NetScope application are stored in:

```text
docs/screenshots/
```

The screenshots demonstrate the application's:

- Main scan interface
- Scan results
- Service details
- Defensive recommendations
- Scan history
- Generated reports

---

## License

This project was created for educational and defensive security purposes.

---

## Author

**Tamil Vanan J**

GitHub Repository:

https://github.com/tamilvananj12-boop/NetScope-Tamil-Vanan-J