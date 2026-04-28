from app.repositories.comment_repository import CommentRepository
from app.repositories.ticket_repository import TicketRepository


class CommentService():
    def __init__(self, comment_repository: CommentRepository, ticket_repository: TicketRepository):
        self.comment_repository = comment_repository
        self.ticket_repository = ticket_repository

    def create_comment(self, ticket_id, comment_data: dict) -> dict:
        self.ticket_repo.get_by_id(ticket_id)
        



