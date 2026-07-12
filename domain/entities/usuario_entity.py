from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    sobrenome: str
    email: str
    senha_hash: str
    id: int | None = None