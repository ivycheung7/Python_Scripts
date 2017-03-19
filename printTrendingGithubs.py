#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

def githubTrend():
    "Script gets the links to each top trending projects from GitHub."
    urlList = []
    html = requests.get("https://github.com/trending")
    soup = BeautifulSoup(html.text, "html.parser")
    for aHeader in soup.find_all('h3'):
        for url in aHeader.find_all('a'):
            urlList.append(str('https://github.com' + url.get('href')))
            #"'https://github.com" +
            #print(url.get('href'))
        print(urlList)

githubTrend()
