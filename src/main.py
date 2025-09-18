# src/main.py
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the API!"}


@app.get("/status")
def get_status():
    """Returns the status of the API."""
    return {"status": "ok"}


# in src/main.py


@app.get("/process/{item_id}")
def process_item(item_id: int):
    """
    Checks if the provided item_id is even or odd.
    """
    if item_id < 0:
        raise HTTPException(
            status_code=400, detail="Item ID must be a positive integer."
        )

    result = "even" if item_id % 2 == 0 else "odd"

    return {"item_id": item_id, "is_even_or_odd": result}
