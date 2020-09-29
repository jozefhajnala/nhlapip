import urllib.request, json

def nhl_get_data_worker(url): 
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

def nhl_get_data(urls):
    return list(map(nhl_get_data_worker, urls))
