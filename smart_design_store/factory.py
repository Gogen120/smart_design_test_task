import os
import asyncio
import logging

from aiohttp import web

from smart_design_store.db import setup_mongo
from smart_design_store.api.routes import routes


async def init_app(loop=None):
    app = web.Application(loop=loop)
    app.on_startup.append(setup_mongo)

    app.add_routes(routes)

    return app


def main():
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(loop))
    web.run_app(app)
