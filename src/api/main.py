from fastapi import FastAPI, HTTPException
import logging

from src.models.schemas import CaloriasResponse, CaloriasRequest

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Calculadora de Calorias")


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/calcular", response_model=CaloriasResponse)
def calcular_frete(dados: CaloriasRequest):
    """
    Calcula as calorias baseado nos alimentos consumidos
    """
    calorias_alimentos_por_grama = {
        "arroz": 1.30,
        "frango": 1.65,
        "feijao": 0.90,
        "macarrao": 1.20,
        "ovo": 1.55,
        "banana": 0.89,
        "maca": 0.52,
        "chocolate": 5.35,
        "queijo": 3.02,
        "pao": 2.64,
    }

    total_calorias = 0

    for alimento in dados.alimentos:
        nome = alimento.nome
        gramas = alimento.gramas

        if nome not in calorias_alimentos_por_grama:
            raise HTTPException(
                status_code=422,
                detail=f"Alimento '{nome}' não encontrado na tabela de calorias",
            )

        total_calorias += (int)(calorias_alimentos_por_grama[nome] * gramas)

        valor_cal = calorias_alimentos_por_grama[nome]
        total_item = valor_cal * gramas

        logger.info(
            f"Processado alimento: nome={nome}, gramas={gramas}, "
            f"cal_por_grama={valor_cal}, subtotal={total_item}"
        )

    logger.info(f"Total de calorias calculado: {total_calorias}")

    return CaloriasResponse(total_calorias=total_calorias)
