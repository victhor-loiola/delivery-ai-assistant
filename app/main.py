from fastapi import FastAPI

app = FastAPI(title="delivery-ai-assistant")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
