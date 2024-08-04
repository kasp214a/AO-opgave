from pydantic import BaseModel
from typing import Optional
class kunder(BaseModel):
    Kunde_ID: int
    kunde_navn: str
    kunde_email: str
    kunde_telefon: Optional[int] = None

class ansatte(BaseModel):
    ansatte_ID: int
    ansatte_navn: str

class ordre(BaseModel):
    ordrenummer: int
    kunde_ID: int
    ordre_dato: str
    ordrelinjer: list = []
    ordre_status: str
    afhentning_lokation: str
    ordre_log: list = []


class ordrelinje(BaseModel):
    ordrelinje_ID: int
    ordrenummer: int
    varenummer: int
    Ansatte_ID: int 
    antal: int 
    ordrelinje_status: bool

class lager(BaseModel):
    varenummer: int
    vare_navn: str
    antal: int
    pris: float
    lager_lokation: str
