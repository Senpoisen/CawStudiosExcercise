from fastapi.middleware.cors import CORSMiddleware



from fastapi import FastAPI
from routes.chat import router as chat_router

app = FastAPI()
app.include_router(chat_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with ["http://localhost:3000"] for safety
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)