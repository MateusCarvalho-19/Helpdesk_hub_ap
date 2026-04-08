from fastapi import FastAPI

# Instância da aplicação FastAPI
app = FastAPI(
    title="Helpdesk Hub API",
    version="1.0.0",
    description="API base para o sistema de Helpdesk Hub"
)

# Base para inclusão futura de routers
# Exemplo:
# from app.routers import tickets
# app.include_router(tickets.router)

@app.get("/")
def root():
    return {"message": "Helpdesk Hub API está no ar!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API operacional"}
