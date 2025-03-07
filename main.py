from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from newspaper import Article

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"]
)


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
