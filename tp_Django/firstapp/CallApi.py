import requests
headers = {'Authorization': 'Token cfa186a1b78c82c51ad90be6589ff2898e21a722'}

url = 'http://127.0.0.1:8000/api/posts/1/'
r = requests.get(url, headers=headers)
print (r.json())