import requests
import html
from bs4 import BeautifulSoup as bs 

url = "https://bharat346.github.io/My_portfolio_bharat/"

#get the html
r = requests.get(url)
html_content = r.content
#print(html_content)

#parse the html
soup = bs(html_content,'html.parser')
#print(soup.prettify)

#tree traversal
title = soup.title
#print(title.string)
#print(type(title))

paras = soup.find_all('p')
#print(paras[1].get_text())
#print(paras[1]['class'])
#print(soup.find_all("p",class_="lead"))

anchors = soup.find_all('a')
all_links = set()
#Get all links 
for link in anchors:
    if(link.get('href') != '#'):
        link_text = link.get('href')
        all_links.add(link)
        print(link_text) 

