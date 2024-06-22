def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "nombre": user["nombre"],
            "email": user["email"]
            }
