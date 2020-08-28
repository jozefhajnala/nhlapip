import unittest
from nhlapip.nhl_url import NhlUrl
from nhlapip.const import NHLAPI_BASEURL

class TestConst(unittest.TestCase):
    def test_ensure_slash_misssing(self):
       self.assertEqual(NhlUrl(baseurl = "foo").ensure_slash().url, "foo/")
    
    def test_ensure_slash_present(self):
       self.assertEqual(NhlUrl(baseurl = "foo/").ensure_slash().url, "foo/")
    
    def test_add_endpoint(self):
       self.assertEqual(NhlUrl().add_endpoint("people").url, NHLAPI_BASEURL + "people")
    
    def test_add_suffixes_single(self):
       self.assertEqual(
           NhlUrl().add_endpoint("people").add_suffixes("100").url,
           NHLAPI_BASEURL + "people" + "/100")
    
    def test_add_suffixes_multiple(self):           
       self.assertEqual(
           NhlUrl().add_endpoint("people").add_suffixes(["100", "200"]).url,
           NHLAPI_BASEURL + "people" + "/100/200")

    def test_get_data(self):           
       url = NhlUrl()
       url.data = 1
       self.assertEqual(url.get_data(), 1)
