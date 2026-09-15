# NetScope — Local Network Service Reporter

A beginner-friendly Flask web application for discovering network services on
localhost and authorized private-network systems.

**Author:** Tamil Vanan J

---

## Overview

NetScope is a defensive network-service discovery tool built with Python and
Flask.

It uses Nmap to identify reachable network services on authorized local or
private-network targets and presents the results through a simple web
interface.

The project was created as a practical learning project to understand:

- Network service discovery
- Open ports and network protocols
- Service and version detection
- Defensive security recommendations
- SQLite database storage
- HTML report generation
- Flask web application development

---

## Features

- Local and private-network target validation
- Nmap-based service discovery
- Open-port detection
- Protocol identification
- Service and version information
- Scan duration reporting
- Defensive security recommendations
- SQLite scan history
- Saved HTML reports
- Simple browser-based interface
- Responsible-use restrictions for public targets

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Flask | Web framework |
| Nmap | Network service discovery |
| python-nmap | Python interface for Nmap |
| SQLite | Scan history storage |
| HTML | Web pages and reports |
| CSS | User interface styling |
| Jinja2 | Flask templates |

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