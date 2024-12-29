import typing as tp

import orjson
from starlette.responses import JSONResponse


class OrJSONResponse(JSONResponse):
    def render(self, content: tp.Any) -> bytes:
        return orjson.dumps(content)
