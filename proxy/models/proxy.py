from datetime import datetime
from sqlmodel import Field, SQLModel
from typing import Optional
from uuid import uuid4

class Proxy(SQLModel, table= True):
    """Represent Proxy in table"""
    id: str = Field(default=str(uuid4()), primary_key=True)
    font: str = Field(nullable=False)
    location: str = Field(nullable=True)
    reability: Optional[float] = Field(default=0.5)
    date_created: datetime = Field(default=datetime.now)
    date_updated: Optional[datetime] = Field()
    