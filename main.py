from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.models
from app.database import engine
from app.routes import router

# Create tables
app.models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Trade Order API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
