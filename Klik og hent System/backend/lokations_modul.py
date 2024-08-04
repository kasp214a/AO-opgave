from fastapi import APIRouter
from database.data import list_ordre, list_ordrelinjer, ordre_statuser
from database import database_models as db

router = APIRouter()

#view af alle test ordre
@router.get("/ordre")
async def ordre():
    return {"here er alle ordre" : list_ordre}

#view af aktive test-ordre
@router.get("/ordre/aktiv")
async def ordre_aktive():
    aktive_ordre = []
    for ordre in list_ordre:
        if ordre.ordre_status == "aktiv":
            aktive_ordre.append(ordre)
    return {"here er alle ordre" : aktive_ordre}
#se ordre detaljer
@router.get("/ordre/{ordrenummer}")
async def ordre_detaljer(ordrenummer: int):
    for ordre in list_ordre:
        if ordrenummer == ordre.ordrenummer:
            return{"here er detaljerne for ordren": ordre}        
    return {"Error" : "En ordre med dette ordrenummer kunne ikke findes"}

#se ordre linje 
@router.get("/ordre/{ordrenummer}/{ordrelinje_ID}")
async def ordrelinje_detaljer(ordrenummer: int, ordrelinje_ID: int):
    for ordrelinje in list_ordrelinjer:
        if ordrelinje_ID == ordrelinje.ordrelinje_ID and ordrenummer == ordrelinje.ordrenummer:
            return{"here er ordrelinjen": ordrelinje}        
    return {"Error" : "En ordre med dette ordrenummer kunne ikke findes"}

#generer en test-ordre
@router.put("/ordre/generate/{ordrenummer}/{kunde_ID}/{afhentning_lokation}/{varenummer}/{antal}/{ordrelinje_id}/{ansatte_id}") 
async def lav_ordre(ordrenummer : int, kunde_ID: int, afhenting: str, varenummer: int, antal: int, ordrelinje_id : int, ansatte_id: int ):
    list_ordre.append(db.ordre(ordrenummer= ordrenummer, kunde_ID=kunde_ID, ordre_dato="02-08-24", ordre_status=ordre_statuser[0], afhentning_lokation=afhenting))
    list_ordrelinjer.append(db.ordrelinje(ordrelinje_ID=ordrelinje_id, ordrenummer=ordrenummer, varenummer=varenummer, antal=antal,Ansatte_ID=ansatte_id ,ordrelinje_status= False))
    ny_ordre = list_ordre[-1]
    ny_ordrelinje = list_ordrelinjer[-1]
    ny_ordre.ordrelinjer.append(ny_ordrelinje)
    return{"ny ordre lavet.": ny_ordre}

#start en ikke aktiv ordre 
@router.put("/ordre/start/{ordrenummer}/{ansatte_ID}")
async def start_ordre(ordrenummer: int, ansatte_ID: int):
    for ordre in list_ordre:
        if ordrenummer == ordre.ordrenummer:
            ordre.ordre_status = ordre_statuser[1]
            ordre.ordre_log.append({"ansatte_ID": ansatte_ID,"Log" :"ansatte ændred ordre status til aktiv"})
            return{"message": "ordren er startet og er nu aktiv"}
    return{"Error": "der kunne ikke findes en ordre med dette nummer"}

#modtage ordrelinje og marker som færdig
@router.put("/ordre/pak/{ordrenummer}/{ordrelinje_ID}/{ansatte_ID}")
async def ordre_pakning(ordrenummer: int, ordrelinje_id: int, ansatte_ID: int):
    for ordrelinje in list_ordrelinjer:
        if ordrenummer == ordrelinje.ordrenummer and ordrelinje_id == ordrelinje.ordrelinje_ID:
            ordrelinje.ordrelinje_status = True
            for ordre in list_ordre:
                if ordrenummer == ordre.ordrenummer:
                    ordre.ordre_log.append({"ansatte_ID": ansatte_ID,"Log" :"ansatte har markeret ordrelinje {} som pakket".format(ordrelinje.ordrelinje_ID)})
            # check om alle ordrelinjer med ordrenummeret har status færdig(True) 
            for ordrelinje in list_ordrelinjer:
                if ordrenummer == ordrelinje.ordrenummer:
                    #hvis nej 
                    if ordrelinje.ordrelinje_status == False:
                        return{"Ordrelinjen melt er afsluttet": ordrelinje}
            for ordre in list_ordre:
                if ordrenummer == ordre.ordrenummer:
                    #set ordre status som afslutet og send mail til kunden
                    ordre.ordre_status = ordre_statuser[2]
                    ordre.ordre_log.append({"ansatte_ID": ansatte_ID,"Log" :"ansatte har pakket alle ordrelinjer og markert dem som færdig", "Log": "en mail er blet sent til kunden om at deres pakke er klar "})
            return{"alle ordre linjer er nu markert afsluttet en mail bliver send til kunden om at deres ordre er klar til af hentning"}
    return {"Error" : "En ordre med dette ordrenummer eller ordrelinje_ID kunne ikke findes"}

#ordren er udlevert
@router.put("/ordre/udlever/{ordrenummer}/{kunde_ID}")
async def udlever_ordre(ordrenummer: int, kunde_ID: int):
    for ordre in list_ordre:
        if ordrenummer == ordre.ordrenummer:
            ordre.ordre_status = ordre_statuser[3]
            ordre.ordre_log.append({"kunde_ID": kunde_ID,"log" : "kunden har registret at de har hentet deres pakke fra boxen"})
            return{"message": "ordren er udleveret til kunden"}
    return{"Error": "der kunne ikke findes en ordre med dette nummer"}
