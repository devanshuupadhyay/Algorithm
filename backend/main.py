# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import your algorithm function
from algorithms.basics import simple_sort

app = FastAPI()

# --- CORS Middleware ---
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models for Data Validation ---
# Define the structure of the incoming request data
class SortRequest(BaseModel):
    numbers: list[int | float]

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Algorithm API is running!"}

@app.post("/api/sort")
def sort_numbers(request: SortRequest):
    """
    API endpoint that receives a list of numbers and returns them sorted.
    """
    sorted_array = simple_sort(request.numbers)
    return {"sorted_numbers": sorted_array}