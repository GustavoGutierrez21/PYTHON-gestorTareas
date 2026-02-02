import json
import time
from typing import Any

import strawberry
from typing import Optional

from core.logging.log_graphql import get_request_metadata
from core.logging.logger import Logger
from accounts.services import UserRoleService
from accounts.graphql.inputs import GetUserRolesInput
from accounts.graphql.types import GetUserRoleResponse

logger = Logger("Roles")


@strawberry.type(
    description="Queries relacionadas con roles de usuario"
)
class UserRoleQuery:
    logger = Logger("Roles")
    service = UserRoleService()
    
    # ============================
    # region obtener roles
    # ============================
    @strawberry.field(
        description="Obtiene todos los roles de usuario, opcionalmente filtrando por ID o nombre."
    )
    @staticmethod
    def get_user_roles(input: Optional[GetUserRolesInput] = None,  info: Any = None) -> GetUserRoleResponse:
        metadata = get_request_metadata(info)
        print(json.dumps(metadata, indent=4)) 
        
        logger.log(f"Buscando roles con los siguientes parametros {input}")
        return UserRoleQuery.service.get_roles(input)
