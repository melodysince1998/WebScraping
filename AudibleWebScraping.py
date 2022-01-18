from bs4 import BeautifulSoup
import requests

url= "https://twitter.com/YearUp/status/1478014600226484224"
response = requests.get(url, timeout=5 )
content = BeautifulSoup(response.content, "html.parser")

print(content)

