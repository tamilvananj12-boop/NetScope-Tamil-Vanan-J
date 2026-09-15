import nmap
def run_service_scan(target):
    scanner=nmap.PortScanner(); scanner.scan(hosts=target, arguments="-sV --version-light -T3")
    result={"hosts":[],"services":[]}
    for host in scanner.all_hosts():
        result["hosts"].append({"address":host,"hostname":scanner[host].hostname(),"state":scanner[host].state()})
        for protocol in scanner[host].all_protocols():
            for port in sorted(scanner[host][protocol].keys()):
                item=scanner[host][protocol][port]
                result["services"].append({"host":host,"protocol":protocol,"port":port,"state":item.get("state","unknown"),"name":item.get("name","unknown"),"product":item.get("product",""),"version":item.get("version","")})
    return result
