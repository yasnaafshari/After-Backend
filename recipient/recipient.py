from pydantic import BaseModel


class Recipient(BaseModel):
    id: int
    name: str
    email: str
    # user: User
