from aiohttp import web
from aiohttp.web_exceptions import HTTPBadRequest, HTTPNotFound
from bson.objectid import InvalidId
from bson import ObjectId
from umongo import ValidationError

from smart_design_store import services, schemas

routes = web.RouteTableDef()


@routes.get('/product')
async def list_products(request: web.Request) -> web.Response:
    products = await services.find_porducts()
    return web.json_response([product.dump() async for product in products], status=200)


@routes.post('/product')
async def create_product(request: web.Request) -> web.Response:
    try:
        schema = schemas.ProductSchema(strict=True)
        payload = schema.load(await request.json()).data
    except ValidationError as error:
        raise HTTPBadRequest(reason=error.messages)

    product = await services.create_product(payload)
    return web.json_response(product.dump(), status=201)


@routes.get('/product/id/{product_id}')
async def get_product_by_id(request: web.Request) -> web.Response:
    product = await services.find_product_by_id(int(request.match_info['product_id']))

    if not product:
        return HTTPNotFound()

    return web.json_response(product.dump(), status=200)


@routes.get('/product/name/{product_name}')
async def get_product_by_name(request: web.Request) -> web.Response:
    products = await services.find_product_by_name(request.match_info['product_name'].lower())

    return web.json_response([product.dump() async for product in products], status=200)


@routes.post('/product/params')
async def get_product_by_params(request: web.Request) -> web.Response:
    payload = await request.json()
    products = await services.find_product_by_param(**payload)

    return web.json_response([product.dump() async for product in products], status=200)
