from pydantic import BaseModel

from app.repositories import TicketRepository


class TicketService(BaseModel):
    repository: TicketRepository  # Injeção de dependência

    def create_ticket(self, ticket_data: dict) -> dict:
        return self.repository.create(ticket_data)

    def get_all_tickets(self) -> list:
        return self.repository.get_all()

    def get_ticket_by_id(self, id: int) -> dict | None:
        return self.repository.get_by_id(id)

    def update_ticket(self, id: int, data: dict) -> dict | None:
        return self.repository.update(id, data)

    def delete_ticket(self, id: int) -> bool:
        return self.repository.delete(id)