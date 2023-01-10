import requests

print(requests.__version__)

print(requests.get('http://google.com/').text)
print(requests.get('https://raw.githubusercontent.com/Alex-Mak-MCW/CMPUT404Lab1/master/filename.py').text)
