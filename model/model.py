from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip: int  
    latitude: float
    longitude: float
