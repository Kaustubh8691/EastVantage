
def addressEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "city": item["city"],
        "state": item["state"],
         "zip": item["zip"],
        "longitude": item["longitude"],
        "latitude": item["latitude"]
    }


def listofaddressEntity(entity) -> list:
    return [addressEntity(item) for item in entity]
