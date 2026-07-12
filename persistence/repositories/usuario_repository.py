import asyncpg

from domain.entities.usuario_entity import Usuario
from domain.ports.usuario_repository_port import UsuarioRepositoryPort

def _map(row) -> Usuario:
    return Usuario(
        id=row["id"],
        nome=row["nome"],
        sobrenome=row["sobrenome"],
        email=row["email"],
        senha_hash=row["senha_hash"]
    )

class UsuarioRepository(UsuarioRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn
    
    async def create(self, usuario: Usuario) -> Usuario:
        row = await self.conn.fetchrow(
            "INSERT INTO usuarios (nome, sobrenome, email, senha_hash) VALUES ($1, $2, $3, $4) RETURNING *",
            usuario.nome, usuario.sobrenome, usuario.email, usuario.senha_hash
            )
        return _map(row)
    
    async def get_by_email(self, email: str) -> Usuario | None:
        row = await self.conn.fetchrow("SELECT * FROM usuarios WHERE email = $1", email)
        return _map(row) if row else None
    
    async def exists_by_email(self, email: str) -> bool:
        row = await self.conn.fetchrow("SELECT 1 FROM usuarios WHERE email = $1", email)
        return row is not None