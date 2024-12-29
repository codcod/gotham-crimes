from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from . import queries
from .models import SessionLocal
from .orjsonresponse import OrJSONResponse


async def add_crime(request: Request):
    with SessionLocal() as db:
        crime = await request.json()
        insertion = queries.create_crime(db, crime)

    if insertion is None:
        raise Exception('Crime not added')

    return OrJSONResponse(
        {
            'description': 'Crime added successfully',
            'status_code': 200,
            'crime_id': insertion.id,
        }
    )


async def get_crimes(request: Request) -> Response:
    with SessionLocal() as db:
        skip = request.query_params.get('skip', '0')
        take = request.query_params.get('take', '100')
        crimes = queries.get_crimes(db, skip=int(skip), take=int(take))

    return OrJSONResponse([c.to_dict() for c in crimes])


async def get_crime(request):
    crime_id = int(request.path_params.get('crime_id'))
    with SessionLocal() as db:
        crime = queries.get_crime(db, crime_id=crime_id)

    if crime is None:
        raise Exception(f'Crime {crime_id} not found')

    return OrJSONResponse(crime.to_dict())


async def update_crime(request):
    crime = request.json()
    crime_id = int(request.path_params.get('crime_id'))
    with SessionLocal() as db:
        updated_crime = queries.update_crime(db, crime_id=crime_id, crime=crime)
    if updated_crime is None:
        raise Exception(f'Crime {crime_id} not found')
    return OrJSONResponse(updated_crime.to_dict())


async def delete_crime(request):
    crime_id = int(request.path_params.get('crime_id'))
    with SessionLocal() as db:
        success = queries.delete_crime(db, crime_id=crime_id)
    if not success:
        raise Exception('Crime not found')
    return OrJSONResponse(
        {'message': 'Crime deleted successfully', 'crime_id': crime_id}
    )


routes = [
    Route('/crimes', get_crimes, methods=['GET']),
    Route('/crimes', add_crime, methods=['POST']),
    Route('/crimes/{crime_id}', get_crime, methods=['GET']),
    Route('/crimes/{crime_id}', update_crime, methods=['PUT']),
    Route('/crimes/{crime_id}', delete_crime, methods=['DELETE']),
]
