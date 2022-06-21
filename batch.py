import asyncio
import aiohttp

from typing import List


class BatchRequest:
    def __init__(self: 'BatchRequest', urls: List[str], method: str = 'GET'):
        self.urls = urls
        self.method = method
        self.results = []

    def get_tasks(self: 'BatchRequest', session: aiohttp.ClientSession):
        tasks = list(
            map(
                lambda url: asyncio.create_task(
                    session.get(url, ssl=False), self.urls
                ),
            )
        )

        return tasks

    async def collect_responses(self: 'BatchRequest'):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=600.0)) as session:
            tasks = self.get_tasks(session)
            responses = await asyncio.gather(*tasks)

            for i, response in enumerate(responses):
                data = await response.json()
                self.results.append(data)

    # TODO: batch every 500 urls
    def run(self: 'BatchRequest'):
        asyncio.run(self.collect_responses())
