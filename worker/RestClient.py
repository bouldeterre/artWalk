from worker.config import getKey
import asyncio
import aiohttp
import os
import urllib.parse
import random
import time


class RestClient(object):
    def __init__(self):
        self.rijkkey = getKey("rijkkey")
        print("RestClient Init")

    def __enter__(self):
        print("RestClient Enter")
        self.loop = asyncio.get_event_loop()
        self.session = self.loop.run_until_complete(self.getSession())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("RestClient Exit")
        self.loop.run_until_complete(self.closeSession())
        self.loop.close()

    async def getSession(self):
        return aiohttp.ClientSession()

    async def closeSession(self):
        await self.session.close()

    async def sendGetRequest(self, req, params):
        print(f"GET:{req}")
        result = await self.session.get(req, params=params)
        print(result.status)
        return result

    async def sendGetRequestJson(self, req, params):
        result = await self.sendGetRequest(req, params)
        return await result.json()
