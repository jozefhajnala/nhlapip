from .const import NHLAPI_BASEURL
from .nhl_get_data import nhl_get_data_worker

class NhlUrl:
    
    def __init__(self, baseurl = NHLAPI_BASEURL):
        self.baseurl = baseurl
        self.url = baseurl
        self.endpoint = None
        self.suffixes = None
        self.data = None
    
    def ensure_slash(self):
        self.url = self.url if self.url.endswith("/") else self.url + "/"
        return self
    
    def add_endpoint(self, endpoint):
        if self.endpoint is None:
            self.ensure_slash()
            self.endpoint = endpoint
            self.url = self.url + endpoint
            return self
        else:
            raise Exception("This NhlUrl already has an endpoint: " + self.endpoint)
    
    def add_suffixes(self, suffixes):
        self.ensure_slash()
        suffix = "/".join(suffixes) if isinstance(suffixes, list) else suffixes
        self.suffixes = suffixes
        self.url = self.url + suffix
        return self
    
    def get_data(self):
        if self.data is None:
            retrievedData = nhl_get_data_worker(self.url)
            self.data = retrievedData
            return retrievedData
        else:
            return self.data
