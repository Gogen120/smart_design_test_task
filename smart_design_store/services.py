from datetime import datetime
from typing import Dict, AsyncIterable

from smart_design_store.models import Product
from smart_design_store.utils import lower_strs


async def create_product(product_data: Dict) -> Product:
    product_counter = await Product.count_documents({})
    product = Product(**lower_strs(product_data), **{'ID': product_counter + 1})
    await product.commit()
    return product


async def find_porducts() -> AsyncIterable[Product]:
    products = Product.find({})
    return products


async def find_product_by_id(product_id: int) -> Product:
    product = await Product.find_one({'ID': product_id})

    return product


async def find_product_by_name(product_name: str) -> AsyncIterable[Product]:
    products = Product.find({'name': {'$regex': product_name}})

    return products


async def find_product_by_param(param_name: str, param_value: str) -> AsyncIterable[Product]:
    products = Product.find({'params.name': param_name, 'params.value': param_value})

    return products
