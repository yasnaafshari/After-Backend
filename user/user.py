from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dateTime
from recipient.recipient import Recipient


class User(BaseModel):
    id: int
    name: Optional[str] = None
    email: str
    password: str
    note: Optional[str] = None
    sendDate: Optional[dateTime] = None
    recipients: Optional[list[Recipient]] = None
