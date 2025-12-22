import json
from openai import OpenAI, OpenAIError
from fastapi import HTTPException
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def analisar_refeicao(texto: str) -> dict:
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Responda somente com JSON válido."},
                {"role": "user", "content": f"""
Analise a refeição e retorne JSON:

{{
  "calorias": number,
  "proteinas": number,
  "carboidratos": number,
  "gorduras": number
}}

Refeição: {texto}
"""}
            ]
        )

        return json.loads(resposta.choices[0].message.content)

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Erro ao interpretar resposta da IA")

    except OpenAIError as e:
        raise HTTPException(status_code=502, detail=str(e))
