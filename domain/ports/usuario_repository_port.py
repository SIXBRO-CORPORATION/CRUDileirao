from abc import ABC, abstractmethod

from domain.entities.usuario_entity import Usuario

class UsuarioRepositoryPort(ABC):

    @abstractmethod
    async def create(self, usuario: Usuario) -> Usuario: ...

    @abstractmethod
    async def get_by_email(self, email: str) -> Usuario | None: ...

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool: ...