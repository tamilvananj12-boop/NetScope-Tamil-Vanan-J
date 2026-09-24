import unittest


class TestScanner(unittest.TestCase):

    def test_basic_scan_result(self):
        result = {
            "port": 80,
            "state": "open",
            "service": "http"
        }

        self.assertEqual(result["state"], "open")
        self.assertEqual(result["port"], 80)

    def test_closed_port(self):
        result = {
            "port": 443,
            "state": "closed",
            "service": "https"
        }

        self.assertEqual(result["state"], "closed")


if __name__ == "__main__":
    unittest.main()