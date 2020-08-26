import unittest
from nhlapip.const import NHLAPI_BASEURL

class TestConst(unittest.TestCase):
    def test_baseurl(self):
        self.assertEqual(NHLAPI_BASEURL, "https://statsapi.web.nhl.com/api/v1/")
