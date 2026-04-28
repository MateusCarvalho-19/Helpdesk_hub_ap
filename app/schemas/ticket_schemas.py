from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class TicketBase(BaseModel):
    title: str
    description: str
    category_id: int
    priority: Literal["baixa", "media", "alta"]
    status: Literal["aberto", "em_andamento", "fechado"]


class TicketCreate(TicketBase):
    pass


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category_id: int | None = None
    priority: Literal["baixa", "media", "alta"] | None = None
    status: Literal["aberto", "em_andamento", "fechado"] | None = None


class TicketResponse(TicketBase):
    id: int
    created_at: datetime
    updated_at: datetime
