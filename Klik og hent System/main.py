from fastapi import FastAPI
from backend import lokations_modul


app = FastAPI()

app.include_router(lokations_modul.router)

@app.get("/")
async def root():
    return {"message" : "Velkommen til klik og hent systemer."}

