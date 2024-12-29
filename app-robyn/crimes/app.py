from robyn import Robyn

from crimes.views import api

app = Robyn(__file__)
app.include_router(api)
app.set_response_header('content-type', 'application/json')

if __name__ == '__main__':
    # create a configured "Session" class
    app.start(host='0.0.0.0', port=8000)
