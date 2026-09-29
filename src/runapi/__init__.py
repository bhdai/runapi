import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok", "env": os.environ.get("APP_ENV", "dev")}


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
