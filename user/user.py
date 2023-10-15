from pydantic import BaseModel
from datetime import datetime as dateTime
from recipient.recipient import Recipient


class User(BaseModel):
    id: int
    username: str
    email: str
    note: str
    sendDate: dateTime
    recipients: list[Recipient]
