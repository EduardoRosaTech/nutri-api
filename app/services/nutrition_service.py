from app.services.openai_client import client
import json

def calcular_nutrientes(texto_refeicao: str) -> dict:
    prompt = f"""
    Você é um nutricionista profissional.

    Analise a refeição abaixo e retorne APENAS um JSON válido no formato:

    {{
      "calorias": number,
      "proteinas": number,
      "carboidratos": number,
      "gorduras": number
    }}

    Refeição: {texto_refeicao}
    """

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    conteudo = resposta.choices[0].message.content

    return json.loads(conteudo)
