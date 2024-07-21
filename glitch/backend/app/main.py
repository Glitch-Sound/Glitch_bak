
from fastapi import FastAPI # type: ignore

import sys
sys.path.append('~/app')

from database import engine, Base
from endpoints.item import router as router_item
from endpoints.user import router as router_user


Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI(title='Glitch', version='0.5.0')
app.include_router(router_item, prefix='/api')
app.include_router(router_user, prefix='/api')
