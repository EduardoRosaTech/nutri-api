from fastapi import APIRouter
from app.schemas.nutrition import RefeicaoInput

router = APIRouter(prefix="/nutrition", tags=["Nutrition"])

TABELA_CALORIAS = {
    "arroz": 130,
    "feijão": 90,
    "frango": 165,
    "ovo": 155,
    "banana": 89,
    "maçã": 52,
    "pão": 265,
}

@router.post("/analyze")
def analisar_refeicao(data: RefeicaoInput):
    alimentos = [a.strip().lower() for a in data.texto.split(",")]

    total = 0
    encontrados = []

    for alimento in alimentos:
        if alimento in TABELA_CALORIAS:
            calorias = TABELA_CALORIAS[alimento]
            total += calorias
            encontrados.append({
                "alimento": alimento,
                "calorias": calorias
            })

    return {
        "total_calorias": total,
        "itens": encontrados,
        "quantidade_itens": len(encontrados)
    }
