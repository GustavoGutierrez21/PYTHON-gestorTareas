import json
import time
import uuid
from typing import Any

def get_request_metadata(info: Any = None) -> dict:
    request_time = time.time()
    id = uuid.uuid4()
    host = ip = headers = request_body = None

    # Obtener request real
    request = getattr(info.context, "request", None) if info else None
    if request is None and isinstance(getattr(info, "context", None), dict):
        request = info.context.get("request") if info.context else None

    if request:
        host = request.get_host()
        ip = request.META.get("REMOTE_ADDR")
        headers = {k: v for k, v in getattr(request, "headers", {}).items()}

        try:
            body_json = json.loads(request.body.decode()) if getattr(request, "body", None) else None
            request_body = {
                "query": body_json.get("query") if body_json else None,
                "variables": body_json.get("variables") if body_json else None
            }
        except Exception:
            request_body = None

    return {
        "id": str(id),
        "host": host,
        "ip": ip,
        "headers": headers,
        "request_time": request_time,
        "request_body": request_body
    }