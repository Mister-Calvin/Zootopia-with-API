import requests

API_KEY = "WVLMZj5jLhWA4NTwxTClSg==U2mNnYWCrgb1D4uk"

def fetch_data(animal_name):
    """ loads API data from the website """
    name = animal_name
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': f"{API_KEY}"})
    as_json = response.json()
    return as_json