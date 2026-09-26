import nmap


def _extract_os(host_data):
    """Return the best OS guess reported by Nmap, if available."""
    matches = host_data.get("osmatch", []) or []
    if not matches:
        return "Not detected"

    best = matches[0]
    name = best.get("name", "Unknown OS")
    accuracy = best.get("accuracy")
    return f"{name} ({accuracy}% match)" if accuracy else name


def run_service_scan(target):
    """Run TCP/UDP port, service/version and OS detection."""
    scanner = nmap.PortScanner()
    arguments = "-sT -sU -sV -O --version-light -T3 --top-ports 1000"

    try:
        scanner.scan(hosts=target, arguments=arguments)
    except nmap.PortScannerError as error:
        # UDP/OS detection can require elevated privileges on some systems.
        # Fall back to a TCP service scan so the app remains usable.
        fallback_arguments = "-sT -sV --version-light -T3 --top-ports 1000"
        scanner = nmap.PortScanner()
        scanner.scan(hosts=target, arguments=fallback_arguments)
        arguments = fallback_arguments
        scan_error = str(error)
    else:
        scan_error = ""

    result = {
        "hosts": [],
        "services": [],
        "scan_arguments": arguments,
        "scan_note": scan_error,
    }

    for host in scanner.all_hosts():
        host_data = scanner[host]
        result["hosts"].append(
            {
                "address": host,
                "hostname": host_data.hostname(),
                "state": host_data.state(),
                "os": _extract_os(host_data),
            }
        )

        for protocol in host_data.all_protocols():
            for port in sorted(host_data[protocol].keys()):
                item = host_data[protocol][port]
                result["services"].append(
                    {
                        "host": host,
                        "protocol": protocol.upper(),
                        "port": port,
                        "state": item.get("state", "unknown"),
                        "name": item.get("name", "unknown"),
                        "product": item.get("product", ""),
                        "version": item.get("version", ""),
                        "extrainfo": item.get("extrainfo", ""),
                    }
                )

    return result
