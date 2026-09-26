import unittest

from scanner.nmap_scanner import _extract_os


class TestScanner(unittest.TestCase):

    def test_basic_scan_result(self):
        result = {
            "port": 80,
            "protocol": "TCP",
            "state": "open",
            "name": "http",
            "version": "Apache",
        }

        self.assertEqual(result["state"], "open")
        self.assertEqual(result["port"], 80)
        self.assertEqual(result["protocol"], "TCP")

    def test_udp_result(self):
        result = {
            "port": 53,
            "protocol": "UDP",
            "state": "open",
            "name": "domain",
        }

        self.assertEqual(result["protocol"], "UDP")
        self.assertEqual(result["port"], 53)

    def test_os_extraction(self):
        host_data = {
            "osmatch": [
                {"name": "Microsoft Windows", "accuracy": "98"}
            ]
        }

        self.assertEqual(_extract_os(host_data), "Microsoft Windows (98% match)")

    def test_os_missing(self):
        self.assertEqual(_extract_os({}), "Not detected")


if __name__ == "__main__":
    unittest.main()
