from smart_design_store.models import Product


ProductSchema = Product.schema.as_marshmallow_schema()


class CreateProductSchema(ProductSchema):
    class Meta:
        fields = ['name']
