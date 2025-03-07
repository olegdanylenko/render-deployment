from fastapi import FastAPI
from pydantic import BaseModel
from newspaper import Article

app = FastAPI()


def article_parsing(url):
    article = Article(url)
    article.download()
    article.parse()

    return article.text


class UrlRequest(BaseModel):
    url: str


@app.post("/process")
async def process_message(request: UrlRequest):
    return {"response": article_parsing(request.url)}
