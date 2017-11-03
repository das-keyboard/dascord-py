import wikipedia


def wikisum(search: str, local: str = 'de', firstsentence: int = 1):
    wikipedia.set_lang(local)
    if firstsentence == 1:
        data = wikipedia.summary(search, sentences=1)
    else:
        data = wikipedia.summary(search)
    if not data:
        return "Nothing found :("
    return data
