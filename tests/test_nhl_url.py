import unittest
from nhlapip.nhl_url import NhlUrl
from nhlapip.const import NHLAPI_BASEURL

class TestNhlUrl(unittest.TestCase):

    def test_paste_dicts(self):
       self.assertEqual(NhlUrl.paste({"one":1, "two":2}), "one=1,two=2")
       self.assertEqual(NhlUrl.paste({"one":1, "two":2}, sep = "&"), "one=1&two=2")
       self.assertEqual(NhlUrl.paste({"one":"1", "two":"2"}), "one=1,two=2")
      
    def test_paste_lists(self):
       self.assertEqual(NhlUrl.paste(["one", "two"]), "one,two")
       self.assertEqual(NhlUrl.paste([1, 2]), "1,2")
      
    def test_ensure_slash_misssing(self):
       self.assertEqual(NhlUrl(baseurl = "foo").ensure_url_endswith("/").url, "foo/")
    
    def test_ensure_slash_present(self):
       self.assertEqual(NhlUrl(baseurl = "foo/").ensure_url_endswith("/").url, "foo/")
    
    def test_add_endpoint(self):
       self.assertEqual(NhlUrl().add_endpoint("people").url, NHLAPI_BASEURL + "people")

    def test_init(self):
       self.assertEqual(
           NhlUrl(endpoint = "people", suffixes = "8451101", params = {"stats": "yearByYear"}).url,
           "https://statsapi.web.nhl.com/api/v1/people/8451101?stats=yearByYear"
       )

    def test_init_int_suffix(self):
       self.assertEqual(
           NhlUrl(endpoint = "people", suffixes = 8451101, params = {"stats": "yearByYear"}).url,
           "https://statsapi.web.nhl.com/api/v1/people/8451101?stats=yearByYear"
       )

    def test_add_suffixes_single_int(self):
       self.assertEqual(
           NhlUrl().add_endpoint("people").add_suffixes(100).url,
           NHLAPI_BASEURL + "people" + "/100")
       
    def test_add_suffixes_single(self):
       self.assertEqual(
           NhlUrl().add_endpoint("people").add_suffixes("100").url,
           NHLAPI_BASEURL + "people" + "/100")
    
    def test_add_suffixes_multiple(self):           
       self.assertEqual(
           NhlUrl().add_endpoint("people").add_suffixes(["100", "200"]).url,
           NHLAPI_BASEURL + "people" + "/100/200")

    def test_addparams_single_new(self):
       self.assertEqual(
           NhlUrl().add_params({"first": "1"}).url,
           NHLAPI_BASEURL[:-1] + "?first=1"
       )
       self.assertEqual(
           NhlUrl().add_params({"first": 1}).url,
           NHLAPI_BASEURL[:-1] + "?first=1"
       )

    def test_addparams_multiple_new(self):
       self.assertEqual(
           NhlUrl().add_params({"first": "1", "second": 2}).url,
           NHLAPI_BASEURL[:-1] + "?first=1&second=2"
       )
       
    def test_addparams_one_append(self):
       testUrl = NhlUrl().add_params({"first": "1", "second": 2})
       self.assertEqual(
          testUrl.add_params({"third":3}).url,
          NHLAPI_BASEURL[:-1] + "?first=1&second=2&third=3"
       )
   
    def test_addparams_multiple_append(self):
       testUrl = NhlUrl().add_params({"first": "1", "second": 2})
       self.assertEqual(
          testUrl.params,
          {"first": "1", "second": 2}
       )
       self.assertEqual(
          testUrl.add_params({"third": 3, "fourth": "4"}).url,
          NHLAPI_BASEURL[:-1] + "?first=1&second=2&third=3&fourth=4"
       )
       self.assertEqual(
          testUrl.params,
          {"first": "1", "second": 2, "third": 3, "fourth": "4"}
       )


    def test_get_data(self):           
       testUrl = NhlUrl()
       testUrl.data = 1
       self.assertEqual(testUrl.get_data(), 1)

