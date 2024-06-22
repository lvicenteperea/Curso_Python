from pydantic import BaseModel


class User(BaseModel):
    id: str | None
    nombre: str
    email: str

