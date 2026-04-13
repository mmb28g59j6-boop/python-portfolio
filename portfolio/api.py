"""Small FastAPI app for the portfolio."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Portfolio API", version="0.1.0")


class EchoRequest(BaseModel):
    message: str


class AddRequest(BaseModel):
    a: float
    b: float


@app.get("/ping")
def ping() -> dict[str, str]:
    """Health check endpoint."""

    return {"status": "ok"}


@app.post("/echo")
def echo(payload: EchoRequest) -> dict[str, str]:
    """Echo the message back to the caller."""

    return {"message": payload.message}


@app.post("/add")
def add(payload: AddRequest) -> dict[str, float]:
    """Add two numbers together."""

    return {"result": payload.a + payload.b}
