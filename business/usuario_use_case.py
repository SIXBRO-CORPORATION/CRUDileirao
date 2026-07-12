from business.security import gerar_hash_senha, verificar_senha
from domain.entities.usuario_entity import Usuario
from domain.exceptions.business_exception import BusinessException
from domain.ports.usuario_repository_port import UsuarioRepositoryPort
from .dtos.usuario_dto import TestarSenhaDTO, UsuarioInputDTO 

class UsuarioUseCase:
    def __init__(self, repository: UsuarioRepositoryPort):
        self.repository = repository

    async def create_usuario(self, dto: UsuarioInputDTO) -> Usuario:
        if await self.repository.exists_by_email(dto.email):
            raise BusinessException("Já existe um usuário com esse email")
        
        usuario = Usuario(
            nome=dto.nome,
            sobrenome=dto.sobrenome,
            email=dto.email,
            senha_hash=gerar_hash_senha(dto.senha),
        )
        return await self.repository.create(usuario)
    
    async def testar_senha(self, dto: TestarSenhaDTO) -> str:
        usuario = await self.repository.get_by_email(dto.email)
        if not usuario:
            raise BusinessException("Usuário não encontrado")
        
        if verificar_senha(dto.senha, usuario.senha_hash):
            return "sucesso"
        return "senha_diferente"