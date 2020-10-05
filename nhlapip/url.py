"""Implementation of the parent NhlUrl class."""
from .const import NHLAPI_BASEURL
from .get_data import nhl_get_data_worker

class NhlUrl:
    """A parent class to be inherited from by all endpoint classes
    """

    def __init__(self, baseurl = NHLAPI_BASEURL, endpoint = None, suffixes = None, params = None):
        self.baseurl = baseurl
        self.url = baseurl
        self.endpoint = None
        self.suffixes = None
        self.params = None
        self.data = None
        self.add_endpoint(endpoint).add_suffixes(suffixes).add_params(params)

    def ensure_url_endswith(self, character):
        """Make use the url property ends with a prescribed character

        Args:
            character (str): The character that the url should end with

        Returns:
            self
        """
        self.url = self.url if self.url.endswith(character) else self.url + character
        return self

    def ensure_url_noendswith(self, character):
        """Make use the url property does not end with a prescribed character"""
        self.url = self.url[:-1] if self.url.endswith(character) else self.url
        return self

    @staticmethod
    def paste(values, sep = ","):
        """Create a single string from different objects

        Args:
            values: A string, integer, dict or list to be concatenated
              into a single string
            sep (str, optional): A character used to separate elements
              in case values has multiple. Defaults to ",".

        Returns:
            str: `values` concatenated into a single string.
        """
        if isinstance(values, str):
            return values
        if isinstance(values, int):
            return str(values)
        if isinstance(values, dict):
            return sep.join("{!s}={!s}".format(key,val) for (key,val) in values.items())
        if isinstance(values, list):
            return sep.join(map(str, values))
        return values

    def add_endpoint(self, endpoint):
        """Add an endpoint to an NhlUrl

        Args:
            endpoint (str): The endpoint to be added

        Raises:
            Exception: An NhlUrl can only have a single endpoint

        Returns:
            self
        """
        if endpoint is None:
            return self
        if self.endpoint is not None:
            raise Exception("This NhlUrl already has an endpoint: " + self.endpoint)

        self.ensure_url_endswith("/")
        self.endpoint = endpoint
        self.url = self.baseurl + endpoint
        return self

    def add_suffixes(self, suffixes):
        """Add suffixes to an NhlUrl

        Args:
            suffixes: The suffixes to be added, can be a single string
              or a list of strings

        Returns:
            self
        """
        if suffixes is None:
            return self
        self.ensure_url_endswith("/")

        suffix = NhlUrl.paste(suffixes, sep = "/")
        self.suffixes = suffixes
        self.url = self.url + suffix
        return self

    def add_params(self, params):
        """Add parameters to an NhlUrl

        Args:
            params: The parameters to be added, usually a dict

        Returns:
            self
        """
        if params is None:
            # Nothing to do
            return self

        self.ensure_url_noendswith("/")

        # Doing something, ensure URL is compatible with adding params
        if self.params is None:
            # No params yet, assign
            self.ensure_url_endswith("?")
            self.params = params
        else:
            # Params present, append
            self.ensure_url_endswith("&")
            self.params.update(params)
        pars_to_add = NhlUrl.paste(params, "&")
        self.url = self.url + pars_to_add
        return self

    def get_data(self):
        """Get the data from url"""
        if self.data is not None:
            return self.data

        print("Getting: " + self.url)
        retrieved_data = nhl_get_data_worker(self.url)
        self.data = retrieved_data
        return retrieved_data
