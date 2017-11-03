from bs4 import BeautifulSoup
import requests
import random


def randomart():
    shop = requests.get('http://shop.draemel.de/shop/')
    content = BeautifulSoup(shop.content, 'html.parser')
    img = content.select('img.product_image')
    select = random.randint(0, len(img) - 1)
    data = [img[select]["alt"], img[select]["src"]]
    if not data[0]:
        return ["Nothing found :(",
                "https://3.bp.blogspot.com/-TSUBSJMQeKM/V0sIG6MOfuI/AAAAAAAABf4/edYpTU8efsQUuAdvgpDRhSslxrt7GnSZwCLcB/s1600/TheSorryGif.gif"]
    return data
