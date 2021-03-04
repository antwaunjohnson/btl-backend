from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Blog(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100, unique=True)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)


Blog_Pydantic = pydantic_model_creator(Blog, name='Blog')
BlogIn_Pydantic = pydantic_model_creator(Blog, name='Blog', exclude_readonly=True)