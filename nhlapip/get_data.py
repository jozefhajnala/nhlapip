"""Wrapper to retrieve the data from NHL API URLs as JSON."""

import urllib.request
import json

def nhl_get_data_worker(url):
    """Get data from an URL

    Args:
        url (str): The URL to retrieve data from

    Returns:
        data: A Python object as created by json.loads
    """
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data
