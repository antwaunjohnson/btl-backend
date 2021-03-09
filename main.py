from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import Blog, Blog_Pydantic, BlogIn_Pydantic


app = FastAPI()

@app.get("/blogs", response_model=Blog_Pydantic)
async def get_blogs():
    return await Blog_Pydantic.from_queryset(Blog.all())


register_tortoise(
    app,
    db_url="postgres:///btldb",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)