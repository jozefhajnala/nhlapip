from .const import NHLAPI_BASEURL
from .nhl_get_data import nhl_get_data_worker

class NhlUrl:
    
    def __init__(self, baseurl = NHLAPI_BASEURL, endpoint = None, suffixes = None, params = None):
        self.baseurl = baseurl
        self.url = baseurl
        self.endpoint = None
        self.suffixes = None
        self.params = None
        self.data = None
        self.add_endpoint(endpoint).add_suffixes(suffixes).add_params(params)
    
    def ensure_url_endswith(self, character):
        self.url = self.url if self.url.endswith(character) else self.url + character
        return self

    def ensure_url_noendswith(self, character):
        self.url = self.url[:-1] if self.url.endswith(character) else self.url
        return self  

    @staticmethod
    def paste(x, sep = ","):
        if isinstance(x, str):
            return x
        if isinstance(x, int):
            return str(x)
        if isinstance(x, dict):
            return sep.join("{!s}={!s}".format(key,val) for (key,val) in x.items())
        if isinstance(x, list):
            return sep.join(map(str, x))
        
    def add_endpoint(self, endpoint):
        if (endpoint is None):
            return self
        if self.endpoint is None:
            self.ensure_url_endswith("/")
            self.endpoint = endpoint
            self.url = self.baseurl + endpoint
            return self
        else:
            raise Exception("This NhlUrl already has an endpoint: " + self.endpoint)
    
    def add_suffixes(self, suffixes):
        if (suffixes is None):
            return self
        self.ensure_url_endswith("/")
        
        suffix = NhlUrl.paste(suffixes, sep = "/")
        self.suffixes = suffixes
        self.url = self.url + suffix
        return self
    
    def add_params(self, params):
        if (params is None):
            # Nothing to do
            return self

        self.ensure_url_noendswith("/")        

        # Doing something, ensure URL is compatible with adding params
        if (self.params is None):
            # No params yet, assign
            self.ensure_url_endswith("?")
            self.params = params
        else:
            # Params present, append
            self.ensure_url_endswith("&")
            self.params.update(params)
        parsToAdd = NhlUrl.paste(params, "&")
        self.url = self.url + parsToAdd
        return self

    def get_data(self):
        if self.data is None:
            print("Getting: " + self.url)
            retrievedData = nhl_get_data_worker(self.url)
            self.data = retrievedData
            return retrievedData
        else:
            return self.data

