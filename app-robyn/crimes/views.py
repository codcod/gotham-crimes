from robyn import Request, SubRouter, jsonify

from . import queries
from .models import SessionLocal

api = SubRouter(__name__, prefix='/api')


@api.post('/crimes')
async def add_crime(request: Request):
    with SessionLocal() as db:
        crime = request.json()
        insertion = queries.create_crime(db, crime)

    if insertion is None:
        raise Exception('Crime not added')

    return {
        'description': 'Crime added successfully',
        'status_code': 200,
    }


@api.get('/crimes')
async def get_crimes(request: Request):
    with SessionLocal() as db:
        skip = request.query_params.get('skip', '0')
        take = request.query_params.get('take', '100')
        crimes = queries.get_crimes(db, skip=int(skip), take=int(take))  # type: ignore

    return jsonify([c.to_dict() for c in crimes])  # type: ignore


@api.get('/crimes/:crime_id', auth_required=True)
async def get_crime(request):
    crime_id = int(request.path_params.get('crime_id'))
    with SessionLocal() as db:
        crime = queries.get_crime(db, crime_id=crime_id)

    if crime is None:
        raise Exception('Crime not found')

    return crime


@api.put('/crimes/:crime_id')
async def update_crime(request):
    crime = request.json()
    crime_id = int(request.path_params.get('crime_id'))
    with SessionLocal() as db:
        updated_crime = queries.update_crime(db, crime_id=crime_id, crime=crime)
    if updated_crime is None:
        raise Exception('Crime not found')
    return updated_crime


@api.delete('/crimes/{crime_id}')
async def delete_crime(request):
    crime_id = int(request.path_params.get('crime_id'))
    with SessionLocal() as db:
        success = queries.delete_crime(db, crime_id=crime_id)
    if not success:
        raise Exception('Crime not found')
    return {'message': 'Crime deleted successfully'}
