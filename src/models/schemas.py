from typing import List

from pydantic import BaseModel, Field


class Alimento(BaseModel):
    nome: str = Field(
        ...,
        min_length=2,
        max_length=50,
        pattern=r"^[a-zA-ZÀ-ÿ\s]+$",  # apenas letras e espaços
        description="Nome do alimento",
    )
    gramas: int = Field(
        ...,
        gt=0,  # > 0
        le=2000,  # limite máximo por item
        description="Quantidade em gramas",
    )


class CaloriasRequest(BaseModel):
    alimentos: List[Alimento]

    class Config:
        json_schema_extra = {
            "example": {
                "alimentos": [
                    {"nome": "arroz", "gramas": 150},
                    {"nome": "feijao", "gramas": 100},
                    {"nome": "frango", "gramas": 100},
                ]
            }
        }


class CaloriasResponse(BaseModel):
    total_calorias: int

    class Config:
        json_schema_extra = {"example": {"total_calorias": 450}}
