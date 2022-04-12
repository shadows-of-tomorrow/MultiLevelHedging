import time
import random
import asyncio


class DummyAPI:

    def __init__(self, tickers):
        self.tickers = tickers
        self.n_tickers = len(tickers)
        self.timer = time.time()
        self.interval = 0.2
        self.interval_async = 0.01

    async def feed(self):
        while True:
            if (time.time() - self.timer) > self.interval:
                self.timer = time.time()
                yield {self.tickers[random.randint(0, self.n_tickers-1)]: random.random()}
                await asyncio.sleep(self.interval_async)