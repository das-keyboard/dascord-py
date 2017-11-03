import lib_pastebin
import secrets
import subprocess
import os


def reload():
    pastebin = lib_pastebin.PasteBin(secrets.PASTEBIN_KEY)
    output = subprocess.getoutput('git pull')
    link = pastebin.paste(output, guest=True, private=0, expire='1H', name='DasCord-Log')
    return link


def restart():
    os.system('python3.6 dascord.py')
    exit(0)


def stop():
    exit(0)
