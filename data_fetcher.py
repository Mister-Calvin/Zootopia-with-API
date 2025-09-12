import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """ loads API data from the website """
    name = animal_name
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': f"{API_KEY}"})
    response_data = response.json()
    return response_data