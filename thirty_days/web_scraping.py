#web scraping is the process of collecting and extracting data from a websites and storing it in our local machine or database
#to start web scraping you need #requests #beautifulsoup4 and a web site
#to target information from a website basic information about html tags,css, classes or ids
import requests
from bs4 import BeautifulSoup
#declRING A URL VARAIBLE
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
#lets use the requests get method to fecth the data from url
response = requests.get(url)
status = response.status_code
print(status)

#using beuatifulsoup to parse content from the page
content = response.content
soup = BeautifulSoup(content,'html.parser')
webtitle = {soup.title}
webbody = soup.body
'''print(soup.title)
print(soup.body)
print(response.status_code)'''
import json
with open('day22exercise1.json','w',encoding='utf-8') as f:
    json.dump(webbody, f, ensure_ascii= False, indent=4)
    
 
