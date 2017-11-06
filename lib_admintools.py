import lib_pastebin
import secrets
import subprocess
import os
import random
from io import StringIO

log = StringIO()


def clearlog():
    global log
    log = StringIO()
    return


def reload():
    name = 'DasCord-UpdateLog_' + str(random.randint(0, 999))
    pastebin = lib_pastebin.PasteBin(secrets.PASTEBIN_KEY)
    output = subprocess.getoutput('git pull')
    link = pastebin.paste(output, guest=True, private=1, expire='1H', name=str(name))
    return link


def restart():
    os.system('python3.6 dascord.py')
    exit(0)


def stop():
    exit(0)


def getlog():
    data = log.getvalue()
    if not data:
        return "No Log avaiable"
    name = 'DasCord-Log_' + str(random.randint(0, 999))
    pastebin = lib_pastebin.PasteBin(secrets.PASTEBIN_KEY)
    link = pastebin.paste(data, guest=True, private=1, expire='1H', name=str(name))
    clearlog()
    return link

