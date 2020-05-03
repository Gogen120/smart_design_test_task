import os
import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from umongo import MotorAsyncIOInstance

instance = MotorAsyncIOInstance()


async def init_mongo():
    mongo_uri = "mongodb://{}:{}".format(
        os.environ.get('MONGO_HOST', 'localhost'),
        os.environ.get('MONGO_PORT', '27017')
    )

    loop = asyncio.get_event_loop()

    conn = AsyncIOMotorClient(
        mongo_uri,
        io_loop=loop
    )
    db_name = os.environ.get('DB_NAME', 'smart_design')
    return conn[db_name]


async def setup_mongo(app):
    mongo = await init_mongo()
    app['db'] = mongo
    instance.init(mongo)

    async def close_mongo(app):
        mongo.client.close()

    app.on_cleanup.append(close_mongo)
