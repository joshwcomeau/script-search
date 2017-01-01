import sys
import requests
import re

from utils import compose

url = sys.argv[1] or 'http://joshwcomeau.github.io/react-flip-move/examples/#/?_k=yduac6'

def pluckJsFromHtmlText(text):
    regex = '\"(.+?\.js)\"'
    return re.findall(regex, text)

def getPageText(url):
    page = requests.get(url)
    return page.text

pluckJsFromUrl = compose(pluckJsFromHtmlText, getPageText)

results = pluckJsFromUrl(url)
print results
print len(results)
