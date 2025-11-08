from fastapi import FastAPI
from routes import router as books_router


app = FastAPI(
    title="Books API",
    description="CRUD service for books"
)

app.include_router(books_router)