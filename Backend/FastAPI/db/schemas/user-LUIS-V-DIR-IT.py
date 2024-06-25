<<<<<<< HEAD
def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "nombre": user["nombre"],
            "email": user["email"]
            }
=======
def user_schema(user_cursor) -> dict:
    return {"id": str(user_cursor["_id"]),
            "nombre": user_cursor["nombre"],
            "email": user_cursor["email"]
            }

def users_schema(users_cursor) -> list:
    return [user_schema(user) for user in users_cursor]
>>>>>>> dc3361e6e5eaf2cf14ac4ac4df9c2c1789318d98
