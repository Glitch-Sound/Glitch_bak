
from fastapi import FastAPI                             # type: ignore
from starlette.middleware.cors import CORSMiddleware    # type: ignore

import sys
sys.path.append('~/app')

from database import engine, Base
from endpoints.item import router as router_item
from endpoints.user import router as router_user
from endpoints.activity import router as router_activity
from endpoints.log import router as router_log


Base.metadata.create_all(bind=engine, checkfirst=True)

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
app.include_router(router_log, prefix='/api')
