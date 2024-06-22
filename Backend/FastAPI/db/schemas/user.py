def user_schema(user_cursor) -> dict:
    return {"id": str(user_cursor["_id"]),
            "nombre": user_cursor["nombre"],
            "email": user_cursor["email"]
            }

def users_schema(users_cursor) -> list:
    return [user_schema(user) for user in users_cursor]
