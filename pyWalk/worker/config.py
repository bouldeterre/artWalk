import json
import getpass

RIJKKEYPHRASE = "What is your Rijksmuseum API key(https://www.rijksmuseum.nl/en/api [Using the API's])"
KEYFILE = ".artkeys"


def setConfig(rijk_key):
    passfile = open(KEYFILE, "w")
    data = {"rijkkey": rijk_key}
    passfile.write(json.dumps(data))
    passfile.close()
    print("Config ok")


def askConfig():
    rijkey = getpass.getpass(RIJKKEYPHRASE)
    setConfig(rijkey)


def getKey(keytype):
    try:
        with open(KEYFILE) as f:
            print(f"{KEYFILE} found")
            data = json.load(f)
            ret = data.get(keytype)
            if ret is not None and ret is not "":
                return ret
    except Exception as e:
        print(f"{KEYFILE} not found")
    askConfig()
