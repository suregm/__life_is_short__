import requests

response = requests.get("http://gomx.win")
print(response.text)

requests.ConnectionError
requests.HTTPError
requests.URLRequired
requests.TooManyRedirects
requests.ConnectTimeout
requests.Timeout