
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import sys
sys.path.append('~/app')

from database import engine, Base, setup_fts
from endpoints.item import router as router_item
from endpoints.user import router as router_user
from endpoints.activity import router as router_activity
from endpoints.summary import router as router_summary


Base.metadata.create_all(bind=engine, checkfirst=True)
setup_fts()

app = FastAPI(title='Glitch', version='0.5.0')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_item, prefix='/api')
app.include_router(router_user, prefix='/api')
app.include_router(router_activity, prefix='/api')
app.include_router(router_summary, prefix='/api')
