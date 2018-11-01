import json


def getKey(keytype):
    with open(".artkeys") as f:
        data = json.load(f)
        ret = data.get(keytype)
        if ret is not None:
            return ret
        raise Exception(f"No ApiKey")
