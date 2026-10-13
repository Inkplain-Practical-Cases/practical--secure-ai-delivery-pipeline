# Application door: mount the release feature without embedding business logic.
from fastapi import FastAPI
from app.features.feature_release.router import router

app = FastAPI(title='Secure AI Delivery Pipeline')
app.include_router(router)

# Persist minimal release HTTP request/outcome audit independently of policy checks.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
