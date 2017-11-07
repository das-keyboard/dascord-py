def calc(erg: str):
    if erg.islower() or erg.isupper():
        return 'Invalid calculation'
    try:
        return eval(erg)
    except ValueError:
        return 'Invalid calculation'
