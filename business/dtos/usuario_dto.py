from pydantic import BaseModel

class UsuarioInputDTO(BaseModel):
    nome: str
    sobrenome: str
    email: str
    senha: str

class TestarSenhaDTO(BaseModel):
    email: str
    senha: str