# Application door: mount the release feature without embedding business logic.
from fastapi import FastAPI
from app.features.feature_release.router import router

app = FastAPI(title='Secure AI Delivery Pipeline')
app.include_router(router)
