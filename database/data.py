from database import database_models as db

#odre status options
ordre_statuser= ["ikke aktiv", "aktiv", "afsluttet", "udlevert"]

afhentnings_lokationer= ["box 1", "box 2", "box 3"]
# set afhentings lokation når man afsluter 

#actual data 
list_kunder =[
    db.kunder(Kunde_ID=1,kunde_navn="bob", kunde_email="test@gmail.com"),
    db.kunder(Kunde_ID=2, kunde_navn="Tue",kunde_email= "test@gmail2.com")
    ]


list_ansatte = [
    db.ansatte (ansatte_ID=214, ansatte_navn="kasper")
]

list_lager = [
    db.lager(varenummer=251, vare_navn="varmepumpe", antal= 300, pris=299.95, lager_lokation="H2"),
    db.lager(varenummer=252, vare_navn="tyveri alarm", antal= 300, pris=250,lager_lokation="G5"),
]

list_ordrelinjer = [
    db.ordrelinje(ordrelinje_ID=12, ordrenummer=11,varenummer=252, Ansatte_ID=214, antal= 2, ordrelinje_status= False),
    db.ordrelinje(ordrelinje_ID=13, ordrenummer=11,varenummer=251, Ansatte_ID=214, antal= 1, ordrelinje_status= False),
    db.ordrelinje(ordrelinje_ID=14, ordrenummer=22,varenummer=251, Ansatte_ID=214, antal= 5, ordrelinje_status= False),
    db.ordrelinje(ordrelinje_ID=15, ordrenummer=33,varenummer=251, Ansatte_ID=214, antal= 3, ordrelinje_status= False),
    
]

list_ordre = [
    db.ordre(ordrenummer=11 , kunde_ID=1, ordre_dato="23-07-24", ordrelinjer=list_ordrelinjer[0:2], ordre_status=ordre_statuser[1], afhentning_lokation=afhentnings_lokationer[0], ordre_log= []),
    db.ordre(ordrenummer=22 , kunde_ID=1, ordre_dato="18-06-24", ordrelinjer=list_ordrelinjer[2:3], ordre_status=ordre_statuser[1], afhentning_lokation=afhentnings_lokationer[1], ordre_log= []),
    db.ordre(ordrenummer=33 , kunde_ID=2, ordre_dato="1-08-24", ordrelinjer=list_ordrelinjer[3:4], ordre_status=ordre_statuser[0], afhentning_lokation=afhentnings_lokationer[2],ordre_log= []),             
]
