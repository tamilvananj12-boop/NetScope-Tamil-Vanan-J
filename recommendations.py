def get_recommendations(open_ports):
    """
    Generate defensive security recommendations
    based on detected open ports.
    """

    recommendations = []

    port_advice = {
        21: "FTP is open. Consider using SFTP/SSH instead of plain FTP.",
        22: "SSH is open. Use strong authentication and disable password login if possible.",
        23: "Telnet is open. Disable Telnet and use SSH instead.",
        25: "SMTP is open. Ensure the mail service is properly secured.",
        53: "DNS is open. Restrict DNS access to trusted networks where possible.",
        80: "HTTP is open. Consider using HTTPS and redirect HTTP traffic.",
        110: "POP3 is open. Prefer encrypted mail protocols such as POP3S.",
        139: "NetBIOS is open. Restrict it to trusted private networks.",
        143: "IMAP is open. Prefer encrypted IMAPS connections.",
        443: "HTTPS is open. Ensure TLS certificates and configuration are up to date.",
        445: "SMB is open. Restrict SMB access and keep the system patched.",
        3306: "MySQL is open. Do not expose database services to untrusted networks.",
        3389: "RDP is open. Restrict access and use strong authentication.",
        5432: "PostgreSQL is open. Restrict database access to trusted hosts.",
        8080: "HTTP alternate port is open. Verify that the web application is secured.",
    }

    for port in open_ports:
        try:
            port_number = int(port)
        except (TypeError, ValueError):
            continue

        if port_number in port_advice:
            recommendations.append({
                "port": port_number,
                "message": port_advice[port_number]
            })

    if not recommendations:
        recommendations.append({
            "port": None,
            "message": "No specific recommendations. Continue monitoring exposed services."
        })

    return recommendations