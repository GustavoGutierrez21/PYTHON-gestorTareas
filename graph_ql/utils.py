import uuid
import json
from django.utils import timezone
from log.models import Log
from strawberry.types import Info


def log_graphql_request(request, info: Info):
    """
    Crea un log mínimo en la tabla Log desde cualquier query o mutation.
    """

    # Generar UUID
    log_id = uuid.uuid4()

    # Host e IP
    host = request.get_host()
    ip = request.META.get("REMOTE_ADDR")

    # Headers
    headers = {k: v for k, v in request.headers.items()}

    # Body
    # Obtener body de la request
    try:
        body = json.loads(request.body.decode("utf-8"))
    except Exception:
        body = {}

    query = body.get("query")
    variables = body.get("variables")

    # Si hay variables, formatearlas a dict simple para imprimir bonito
    if variables is None:
        variables_formatted = {}
    else:
        variables_formatted = {k: v for k, v in variables.items()}

    request_body = {
        "query": query,
        "variables": variables_formatted,
        "operation": body.get("operationName"),
        "resolver_name": info._field.name,
        # 'QUERY' o 'MUTATION'
        "operation_type": str(info._raw_info.operation.operation),
    }

    # Request time
    request_time = timezone.now()

    # Crear log

    log = {
        "id_log": str(log_id),
        "host": host,
        "ip": ip,
        "headers": headers,
        "request_body": request_body,
        "request_time": str(request_time),
    }
    # print(json.dumps(log, indent=4))
    return log
