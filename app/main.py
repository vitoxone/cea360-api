# app/main.py
from fastapi import FastAPI
from app.routes import training
from app.models import Training, TrainingAsset

app = FastAPI(
    title="CEA360 API",
    version="1.0.0",
    description="""
CEA360 es una plataforma de entrenamientos para cuidadores, madres y padres de niños con diagnóstico TEA.

🔹 Puedes listar, crear y actualizar entrenamientos.  
🔹 Los entrenamientos pueden ser gratuitos o de pago.  
🔹 El acceso se gestiona por email o código de suscripción.  
""",
    contact={
        "name": "Equipo CEA360",
        "url": "https://cea360.cl",
        "email": "soporte@cea360.cl",
    },
    terms_of_service="https://cea360.cl/terminos",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Routers
app.include_router(training.router)

@app.get("/")
def root():
    return {"message": "CEA360 API is running"}