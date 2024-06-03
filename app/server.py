import os.path
from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse, RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from sqlmodel import SQLModel, create_engine

from app.config import ENVIRONMENT
from app.auth import use_auth


app = FastAPI()


#
# Attempt to retrieve a file.
# If the file is not found, attempt to retrieve it
# relative to the provided directory for static assets.
#
class StaticFilesMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, directory='static'):
        super().__init__(app)
        self.directory = directory

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if response.status_code == 404:
            path = os.path.join(self.directory, request.url.path.lstrip('/'))
            if os.path.exists(path):
                return FileResponse(path)
        return response


#
# Ensure CORS work while using the Vite dev server
#
if ENVIRONMENT == 'development':
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*'])
else:
    app.add_middleware(StaticFilesMiddleware, 
                       directory=os.path.join(__file__, '../frontend/dist'))


#
# Register different apps
#
use_auth(app)


#
# Serve Frontend bundle
#
@app.get('/{anything:path}')
async def index(request: Request):
    if ENVIRONMENT == 'development':
        params = ''
        if len(request.query_params.keys()) > 0:
            params = '?' + '&'.join([f'{k}={v}' for k,v in request.query_params.items()])
        return RedirectResponse('http://localhost:4321/' + params)
    else:
        if '.' in request.url.path.lstrip('/').split('?')[0]:
            return Response(status_code=404)
        return FileResponse('frontend/dist/index.html')

