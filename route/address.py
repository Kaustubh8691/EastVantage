from fastapi import APIRouter

from model.address import Address
from config.db import conn
from schema.address import addressEntity, listofaddressEntity
from bson import ObjectId
from Distance import getDistance

address = APIRouter()

@address.get("/address")
async def find_all():
    print(conn.local.user.find())
    print(listofaddressEntity(conn.local.address.find()))
    return listofaddressEntity(conn.local.address.find())

@address.post("/address")
async def add_new_data(address: Address):
    if address.latitude is None or address.longitude is None:
        return {"error": "Latitude and Longitude are required"}
    if address.latitude < -90 or address.latitude > 90:
        return {"error": "Latitude must be between -90 and 90"}
    if address.longitude < -180 or address.longitude > 180:
        return {"error": "Longitude must be between -180 and 180"}
    conn.local.address.insert_one(dict(address))
    return listofaddressEntity(conn.local.address.find())

@address.delete("/{id}")
async def delete_address_data(id, address: Address):
    return addressEntity(conn.local.address.find_one_and_delete({"_id": ObjectId(id)}))

@address.put("/{id}")
async def update_address_data(id, address: Address):
    if address.latitude is None or address.longitude is None:
        return {"error": "Latitude and Longitude are required"}
    if address.latitude < -90 or address.latitude > 90:
        return {"error": "Latitude must be between -90 and 90"}
    if address.longitude < -180 or address.longitude > 180:
        return {"error": "Longitude must be between -180 and 180"}
    conn.local.address.find_one_and_update({"_id": ObjectId(id)},{'$set': dict(address)})
    return addressEntity(conn.local.address.find_one({"_id": ObjectId(id)}))




@address.get("/totalrange")
async def get_range(latitude1, longitude1, distance):

    latitude1 = float(latitude1)
    longitude1 = float(longitude1)
    distance = float(distance)
    if latitude1 < -90 or latitude1 > 90:
        return {"error": "Latitude have to -90 and 90"}
    if longitude1 < -180 or longitude1 > 180:
        return {"error": "Longitude have to -180 and 180"}
    
    if distance < 0:
        return {"error": "Invalid Distance"}
    
    
    for address in conn.local.address.find(): 
        if getDistance(latitude1, longitude1, address["latitude"], address["longitude"]) <= distance:
            return addressEntity(address)