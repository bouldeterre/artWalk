import json
import getpass
import os

RIJKKEYPHRASE = "What is your Rijksmuseum API key(https://www.rijksmuseum.nl/en/api [Using the API's])"
KEYFILE = ".artkeys"
curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYPATH = os.path.join(curpath, KEYFILE)


def setConfig(rijk_key):
    passfile = open(KEYPATH, "w")
    data = {"rijkkey": rijk_key}
    passfile.write(json.dumps(data))
    passfile.close()
    print("Config ok")


def askConfig():
    rijkey = getpass.getpass(RIJKKEYPHRASE)
    setConfig(rijkey)


def getKey(keytype):
    try:
        with open(KEYPATH) as f:
            print(f"{KEYPATH} found")
            data = json.load(f)
            ret = data.get(keytype)
            if ret is not None and ret is not "":
                return ret
    except Exception as e:
        print(f"{KEYPATH} not found")
    askConfig()
