import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import unittest

from quilt_canary_port.python_port import fnv1a_64, verify, CANARY_INPUT, EXPECTED


class TestCanary(unittest.TestCase):

    def test_canary_value(self):
        self.assertEqual(fnv1a_64(CANARY_INPUT), EXPECTED)

    def test_verify(self):
        self.assertTrue(verify())

    def test_deterministic(self):
        h1 = fnv1a_64(CANARY_INPUT)
        h2 = fnv1a_64(CANARY_INPUT)
        self.assertEqual(h1, h2)

    def test_empty_string(self):
        h = fnv1a_64("")
        # FNV-1a offset basis for empty string
        self.assertEqual(h, 0xcbf29ce484222325)


if __name__ == "__main__":
    unittest.main()
