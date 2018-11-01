from worker.config import getKey
import asyncio
import aiohttp
import os
import urllib.parse

api = "https://www.rijksmuseum.nl/api/nl/collection/"
chunk_size = 200


class PaintClient(object):
    def __init__(self):
        self.rijkkey = getKey("rijkkey")

        print("Init")

    def __enter__(self):
        print("Enter")
        self.loop = asyncio.get_event_loop()
        self.session = self.loop.run_until_complete(self.getSession())
        return self

    async def getSession(self):
        return aiohttp.ClientSession()

    async def closeSession(self):
        await self.session.close()

    async def sendGetRequestJson(self, req, params):
        print(f"GET:{req} with:{params}")
        result = await self.session.get(req, params=params)
        print(result.status)
        return await result.json()

    async def sendGetRequest(self, req):
        print(f"GET:{req}")
        result = await self.session.get(req)
        print(result.status)
        return result

    async def printUrl(self, url, filename):
        curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(curpath, "assets")
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, filename)
        print(filepath)
        resp = await self.sendGetRequest(url)
        with open(filepath, "wb") as fd:
            while True:
                chunk = await resp.content.read(chunk_size)
                if not chunk:
                    break
                fd.write(chunk)

    def getPaint(self, paintName):
        print("getPaint")
        req = urllib.parse.urljoin(api, paintName)
        parameters = {"key": self.rijkkey, "format": "json"}
        result = self.loop.run_until_complete(self.sendGetRequestJson(req, parameters))
        url = result.get("artObject").get("webImage").get("url")
        result = self.loop.run_until_complete(self.printUrl(url, f"{paintName}.jpg"))

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        self.loop.run_until_complete(self.closeSession())
        self.loop.close()
