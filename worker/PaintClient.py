import asyncio
import aiohttp
import os
import urllib.parse
import random
import time
from worker.config import getKey
from worker.RestClient import RestClient

api = "https://www.rijksmuseum.nl/api/nl/collection/"
chunk_size = 200


class PaintClient(RestClient):
    def __init__(self):
        RestClient.__init__(self)
        self.rijkkey = getKey("rijkkey")
        print("PaintClient Init")

    def __enter__(self):
        RestClient.__enter__(self)
        print("PaintClient Enter")
        return self

    async def printUrlAsync(self, url, filename):
        curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(curpath, "assets")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, filename)
        print(filepath)
        resp = await self.sendGetRequest(url, {})
        with open(filepath, "wb") as fd:
            while True:
                chunk = await resp.content.read(chunk_size)
                if not chunk:
                    break
                fd.write(chunk)

    def printUrl(self, url, filename):
        result = self.loop.run_until_complete(
            self.printUrlAsync(url, f"{time.time()}_{filename}.jpg")
        )

    def getPaint(self, paintName):
        print("getPaint")
        req = urllib.parse.urljoin(api, paintName)
        parameters = {"key": self.rijkkey, "format": "json"}
        result = self.loop.run_until_complete(self.sendGetRequestJson(req, parameters))
        url = result.get("artObject").get("webImage").get("url")
        self.printUrl(url, paintName)

    def getRandomPaint(self):
        key: AyVUm1zo
        parameters = {
            "key": self.rijkkey,
            "format": "json",
            "type": "schilderij",
            "imgonly": "True",
            "ps": 1,
            "p": 1,
        }
        result = self.loop.run_until_complete(self.sendGetRequestJson(api, parameters))
        maxpaintings = result.get("count")
        page = random.randint(0, maxpaintings)
        parameters["p"] = page
        result = self.loop.run_until_complete(self.sendGetRequestJson(api, parameters))
        artObject = result.get("artObjects")[0]
        id = artObject.get("id")
        title = artObject.get("title")
        url = artObject.get("webImage").get("url")
        print(id)
        print(artObject.get("objectNumber"))
        print(title)
        print(url)
        return id, title, url

    def __exit__(self, exc_type, exc_val, exc_tb):
        RestClient.__exit__(self, exc_type, exc_val, exc_tb)
