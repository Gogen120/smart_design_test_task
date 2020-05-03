from smart_design_store.models import Product

PRODUCT_DATA = [
    {
        'name': 'iphone20',
        'description': 'brand new iphone',
        'params': [
            {
                'name': 'size',
                'value': 20,
            },
            {
                'name': 'color',
                'value': 'black',
            },
        ]
    },
    {
        'name': 'iphone10',
        'description': 'old iphone',
        'params': [
            {
                'name': 'size',
                'value': 10,
            },
            {
                'name': 'color',
                'value': 'white',
            },
        ]
    },
    {
        'name': 'iphone20',
        'description': 'brand new iphone',
        'params': [
            {
                'name': 'size',
                'value': 20,
            },
            {
                'name': 'color',
                'value': 'white',
            },
        ]
    },
    {
        'name': 'samsung galaxy',
        'description': 'not an iphone',
        'params': [
            {
                'name': 'size',
                'value': 30,
            },
            {
                'name': 'color',
                'value': 'black',
            },
        ]
    },
]

async def create_products():
    for product_payload in PRODUCT_DATA:
        product = Product(**product_payload)
        await product.commit()
