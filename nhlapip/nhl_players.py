from .nhl_url import NhlUrl
from .const import NHLAPI_BASEURL

class Player:
    
    def __init__(self, id):
        self.id = id
        self.url = NhlUrl().add_endpoint("people").add_suffixes(id)
        self.data = None
    
    def get_data(self):
        self.data = self.url.get_data()
        return self.data
