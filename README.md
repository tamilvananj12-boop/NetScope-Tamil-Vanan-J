# NetScope - Local Network Service Reporter

**Author:** Tamil Vanan J

An original beginner-friendly Flask application for defensive network-service discovery on systems you own or are authorized to test.

## Features
- Local/private target validation
- Nmap service discovery
- Open-port summary
- Service/version information
- Scan duration
- Defensive recommendations
- SQLite scan history
- HTML report generation

## Technology
Python, Flask, python-nmap, SQLite, HTML/CSS and Jinja2.

## Run
1. Install Python 3.10+.
2. Install Nmap and ensure `nmap` is available in the terminal.
3. Create a virtual environment.
4. Run `pip install -r requirements.txt`.
5. Run `python app.py`.
6. Open the local Flask address shown in the terminal.

## Responsible Use
Only scan localhost, private-network systems, or systems for which you have explicit permission. Public targets are rejected by the application.
