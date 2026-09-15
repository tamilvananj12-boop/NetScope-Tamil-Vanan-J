import ipaddress, socket
def is_allowed_target(value):
    value=value.strip()
    if not value: return False
    if value.lower() in {"localhost","127.0.0.1","::1"}: return True
    try:
        address=ipaddress.ip_address(value); return address.is_private or address.is_loopback
    except ValueError:
        try:
            address=ipaddress.ip_address(socket.gethostbyname(value)); return address.is_private or address.is_loopback
        except (socket.gaierror,ValueError): return False
