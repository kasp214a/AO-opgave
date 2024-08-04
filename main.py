from fastapi import FastAPI
from backend import lokations_modul


app = FastAPI()

app.include_router(lokations_modul.router)

@app.get("/")
async def root():
    return {
        "Velkomst message" : "Velkommen til klik og hent systemer.",
        "info" : "here er en liste af de paths der kan til gås",
        "/docs" : "docomentation siden hvor det er muligt at genere ordre og ændre status på eksiternde ordre",
        "/ordre" : "viser alle ordre i systemer og deres ordre linjer",
        "/ordre/aktiv" : "viser all aktive ordre i systemet",
        "/ordre/'ordrenummer'" : "viser information om ordren med det givede ordrenummer",
        "/ordre/'ordrenummer'/'ordrelinje_ID'" : "viser ordrelinjen fra den valge ordre"
                  
        }

