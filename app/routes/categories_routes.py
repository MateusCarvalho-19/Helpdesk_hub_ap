from fastapi import APIRouter, HTTPException, status, Depends

from app.schemas.category_schemas import CategoryCreate, CategoryResponse
from app.services import CategoryService
from app.repositories import CategoryRepository

router = APIRouter(prefix="/categories", tags=["categories"])


def get_category_service() -> CategoryService:
    """Provider que cria o serviço com o repositório injetado"""
    repository = CategoryRepository()
    return CategoryService(repository=repository)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    """Cria uma nova categoria"""
    return service.create_category(category.model_dump())


@router.get("/", response_model=list[CategoryResponse])
def list_categories(service: CategoryService = Depends(get_category_service)):
    """Lista todas as categorias"""
    return service.get_all_categories()


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, service: CategoryService = Depends(get_category_service)):
    """Obtém uma categoria pelo ID"""
    category = service.get_category_by_id(category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {category_id} não encontrada"
        )
    return category


@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    """Atualiza uma categoria"""
    updated = service.update_category(category_id, category.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {category_id} não encontrada"
        )
    return updated


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, service: CategoryService = Depends(get_category_service)):
    """Elimina uma categoria"""
    deleted = service.delete_category(category_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria com ID {category_id} não encontrada"
        )