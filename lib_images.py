import json
import requests
import secrets

key = secrets.GOOGLE_KEY
id = secrets.GOOGLE_ID


def img(search :str):
    search = search.replace(' ', '%20')
    searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
                search + "&start=1&num=1&key=" + key + "&cx=" + id + \
                "&searchType=image"
    r = requests.get(searchUrl)
    response = r.content.decode('utf-8')
    result = json.loads(response)
    img = result['items'][0]['link']
    if not img:
        return "No Image found :("
    return img

