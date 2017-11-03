import json
import requests
import secrets
import random

key = secrets.GOOGLE_KEY
id = secrets.GOOGLE_ID


def img(search: str, num: int):
    search = search.replace(' ', '%20')
    if num == 0:
        index = 1
        count = 5
        select = random.randint(0, 4)
    else:
        index = num
        count = 1
        select = 0
    searchurl = "https://www.googleapis.com/customsearch/v1?q=" + \
                search + "&start=" + index + "&num=" + count + "&key=" + key + "&cx=" + id + \
                "&searchType=image"
    r = requests.get(searchurl)
    response = r.content.decode('utf-8')
    result = json.loads(response)
    img = result['items'][select]['link']
    if not img:
        return "No Image found :("
    return img

