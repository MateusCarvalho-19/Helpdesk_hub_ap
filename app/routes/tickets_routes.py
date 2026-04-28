from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas.ticket_schemas import TicketCreate, TicketResponse, TicketUpdate
from app.services import TicketService, CategoryService
from app.repositories import TicketRepository, CategoryRepository

router = APIRouter(prefix="/tickets", tags=["tickets"])


def get_ticket_service() -> TicketService:
    """Provider que cria o serviço com o repositório injetado"""
    repository = TicketRepository()
    return TicketService(repository=repository)


def get_category_service() -> CategoryService:
    """Provider para validar categoria"""
    repository = CategoryRepository()
    return CategoryService(repository=repository)


@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(
    ticket: TicketCreate,
    ticket_service: TicketService = Depends(get_ticket_service),
    category_service: CategoryService = Depends(get_category_service)
):
    """Cria um novo ticket (valida se category_id existe)"""
    # Validar se a categoria existe
    category = category_service.get_category_by_id(ticket.category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {ticket.category_id} não encontrada"
        )
    
    return ticket_service.create_ticket(ticket.model_dump())


@router.get("/", response_model=list[TicketResponse])
def list_tickets(ticket_service: TicketService = Depends(get_ticket_service)):
    """Lista todos os tickets"""
    return ticket_service.get_all_tickets()


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, ticket_service: TicketService = Depends(get_ticket_service)):
    """Obtém um ticket pelo ID"""
    ticket = ticket_service.get_ticket_by_id(ticket_id)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket com ID {ticket_id} não encontrado"
        )
    return ticket


@router.patch("/{ticket_id}", response_model=TicketResponse)
def update_ticket(
    ticket_id: int,
    ticket: TicketUpdate,
    ticket_service: TicketService = Depends(get_ticket_service)
):
    """Atualiza um ticket (parcial)"""
    # Filtrar apenas campos que foram enviados (não None)
    update_data = ticket.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum dado fornecido para atualização"
        )
    
    updated = ticket_service.update_ticket(ticket_id, update_data)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ticket com ID {ticket_id} não encontrado"
        )
    return updated