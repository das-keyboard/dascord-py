from bs4 import BeautifulSoup
import requests

def gethottestimg(num : int):
    hot_site = requests.get('https://9gag.com/')
    content = BeautifulSoup(hot_site.content, 'html.parser')
    img = content.select('img[class=badge-item-img]')
    img = img[num]
    hot = [img['alt'], img['src']]
    return hot

def getnewestimg(num : int):
    hot_site = requests.get('https://9gag.com/fresh')
    content = BeautifulSoup(hot_site.content, 'html.parser')
    img = content.select('img[class=badge-item-img]')
    img = img[num]
    hot = [img['alt'], img['src']]
    return hot

def getimg(sec : str, num : int):
    hot_site = requests.get('https://9gag.com/' + sec)
    content = BeautifulSoup(hot_site.content, 'html.parser')
    img = content.select('img[class=badge-item-img]')
    img = img[num]
    hot = [img['alt'], img['src']]
    return hot
