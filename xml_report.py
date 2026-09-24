import xml.etree.ElementTree as ET


def generate_xml_report(filename, target, scan_results):
    """
    Generate an XML report containing network scan results.
    """

    root = ET.Element("netscope_report")

    target_element = ET.SubElement(root, "target")
    target_element.text = str(target)

    results_element = ET.SubElement(root, "scan_results")

    for result in scan_results or []:
        result_element = ET.SubElement(results_element, "service")

        if isinstance(result, dict):
            port = result.get("port", "")
            state = result.get("state", "open")
            service = result.get("service", "")
            version = result.get("version", "")

            ET.SubElement(
                result_element, "port"
            ).text = str(port)

            ET.SubElement(
                result_element, "state"
            ).text = str(state)

            ET.SubElement(
                result_element, "service_name"
            ).text = str(service)

            ET.SubElement(
                result_element, "version"
            ).text = str(version)

        else:
            ET.SubElement(
                result_element, "details"
            ).text = str(result)

    tree = ET.ElementTree(root)

    try:
        ET.indent(tree, space="  ")
    except AttributeError:
        pass

    tree.write(
        filename,
        encoding="utf-8",
        xml_declaration=True
    )

    return filename