def addressEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "city": item["city"],
        "zip": item["zip"],
        "state": item["state"],
        "longitude": item["longitude"],
        "latitude": item["latitude"],
    }


def listaddressEntity(entity) -> list:
    return [addressEntity(item) for item in entity]