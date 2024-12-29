from contextlib import asynccontextmanager

from starlette.applications import Starlette
from starlette.routing import Mount

from . import views


@asynccontextmanager
async def lifespan(app):
    print('Startup')
    yield
    print('Shutdown')


routes = [Mount('/api', routes=views.routes)]

app = Starlette(debug=True, lifespan=lifespan, routes=routes)
