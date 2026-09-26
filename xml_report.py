import xml.etree.ElementTree as ET


def generate_xml_report(filename, target, scan_results, hosts=None):
    """Generate a structured XML report containing scan results."""
    root = ET.Element("netscope_report")
    ET.SubElement(root, "target").text = str(target)

    hosts_element = ET.SubElement(root, "hosts")
    for host in hosts or []:
        host_element = ET.SubElement(hosts_element, "host")
        ET.SubElement(host_element, "address").text = str(host.get("address", ""))
        ET.SubElement(host_element, "hostname").text = str(host.get("hostname", ""))
        ET.SubElement(host_element, "state").text = str(host.get("state", ""))
        ET.SubElement(host_element, "operating_system").text = str(
            host.get("os", "Not detected")
        )

    results_element = ET.SubElement(root, "scan_results")
    for result in scan_results or []:
        service_element = ET.SubElement(results_element, "service")
        ET.SubElement(service_element, "port").text = str(result.get("port", ""))
        ET.SubElement(service_element, "protocol").text = str(
            result.get("protocol", "")
        )
        ET.SubElement(service_element, "state").text = str(
            result.get("state", "unknown")
        )
        ET.SubElement(service_element, "service_name").text = str(
            result.get("name", result.get("service", ""))
        )
        ET.SubElement(service_element, "product").text = str(
            result.get("product", "")
        )
        ET.SubElement(service_element, "version").text = str(
            result.get("version", "")
        )
        ET.SubElement(service_element, "extra_info").text = str(
            result.get("extrainfo", "")
        )

    tree = ET.ElementTree(root)
    try:
        ET.indent(tree, space="  ")
    except AttributeError:
        pass

    tree.write(filename, encoding="utf-8", xml_declaration=True)
    return filename
