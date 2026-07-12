import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
from api.schemas.usuario_schema import TestarSenhaSchema, UsuarioSchema
from business.dtos.usuario_dto import TestarSenhaDTO, UsuarioInputDTO
from business.usuario_use_case import UsuarioUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.usuario_repository import UsuarioRepository

router = APIRouter(prefix="/usuarios", tags=["Usuario"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> UsuarioUseCase:
    return UsuarioUseCase(UsuarioRepository(conn))


@router.post("/", response_model=ApiResponse[UsuarioSchema], status_code=201)
async def criar_usuario(dto: UsuarioInputDTO, usecase: UsuarioUseCase = Depends(get_use_case)):
    data = await usecase.create_usuario(dto)
    return ApiResponse.success_response(data=data)


@router.post("/testar-senha", response_model=ApiResponse[TestarSenhaSchema])
async def testar_senha(dto: TestarSenhaDTO, usecase: UsuarioUseCase = Depends(get_use_case)):
    resultado = await usecase.testar_senha(dto)
    return ApiResponse.success_response(data=TestarSenhaSchema(resultado=resultado))