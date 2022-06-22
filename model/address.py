from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip: str   
    latitude: float
    longitude: float