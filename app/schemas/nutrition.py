from pydantic import BaseModel, Field

class RefeicaoInput(BaseModel):
    texto: str = Field(
        ...,
        min_length=3,
        example="arroz, feijão, frango"
    )
