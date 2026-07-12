from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    sobrenome: str
    email: str

    model_config = {"from_attributes": True}

class TestarSenhaSchema(BaseModel):
    resultado: str