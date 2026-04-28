from pydantic import BaseModel
from datetime import datetime

class CommentBase (BaseModel):
    ticket_id: int
    author_name: str
    content: str

class CommentCreate (CommentBase):
    ticket_id: int
    author_name: str
    content: str

class CommentResponse (CommentBase):
    ticket_id: int
    author_name: str
    content: str
    id: int
    created_at: datetime
