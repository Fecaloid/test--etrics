from nanoid import generate
from tortoise import fields
from tortoise.models import Model


class TestModel(Model):
    id = fields.CharField(pk=True, max_length=22, default=generate)
    title = fields.CharField(max_length=50)

    class Meta:
        table = 'testmodel'
