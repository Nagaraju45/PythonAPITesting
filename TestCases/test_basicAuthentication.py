import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get("https://github.com/login", auth = HTTPBasicAuth("nagarajubollikonda264@gmail.com", "Nagaraju_45"))
    print(response.text)