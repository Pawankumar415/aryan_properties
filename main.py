from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from api.endpoints import (user_rouetr,  property_router, propertyTypes_router, leaseSale_router, description_router, log_router,client_router,property_with_hierarchy_router,
                           furnished_property_router, area_router)
# Base.metadata.create_all(bind=engine)

# app = FastAPI(root_path="/aryan_properties")
app = FastAPI(
    docs_url=None,
    redoc_url=None
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = FastAPI.openapi(app)  
    openapi_schema["info"]["title"] = "Aryans Properties"
    openapi_schema["info"]["version"] = "1.1.0"
    openapi_schema["info"]["description"] = "This API serves as the backend for Aryans Properties."
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user_rouetr, prefix="/api", tags=["User Routes"])
app.include_router(property_with_hierarchy_router, prefix="/api", tags=["property with hierarchy Routes"])
app.include_router(property_router, prefix="/api", tags=["Property Routes"])
#app.include_router(propertyDetails_router, prefix="/api", tags=["Property Details Routes"])
app.include_router(propertyTypes_router, prefix="/api", tags=["Property Types Routes"])
app.include_router(furnished_property_router, prefix="/api", tags=["furnished property Routes"])
app.include_router(leaseSale_router, prefix="/api", tags=["Lease Sale Routes"])
app.include_router(description_router, prefix="/api", tags=["Description Routes"])
# app.include_router(propertyContacts_router, prefix="/api", tags=["Property Contacts Routes"])
# app.include_router(city_router, prefix="/api", tags=["City Routes"])
# app.include_router(sublocation_router, prefix="/api", tags=["Sublocation Routes"])
app.include_router(area_router, prefix="/api", tags=["Area Routes"])
#app.include_router(companies_router, prefix="/api", tags=["Companies Routes"])
#app.include_router(underconstruction_router, prefix="/api", tags=["Underconstruction Routes"])
app.include_router(client_router, prefix="/api", tags=["client Routes"])
app.include_router(log_router, prefix="/api", tags=["Logs Routes"])



from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse
import secrets


security = HTTPBasic()
REALM = "swagger"

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "12345678")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": f'Basic realm="{REALM}"'},
        )

# ✅ /docs with Basic Auth
@app.get("/docs", include_in_schema=False)
def custom_docs(credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Swagger UI")

# ✅ /redoc with Basic Auth
@app.get("/redoc", include_in_schema=False)
def custom_redoc(credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    return get_redoc_html(openapi_url="/openapi.json", title="Redoc")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload= True, host="0.0.0.0")






# uvicorn main:app --port 8004 --host 0.0.0.0 --reload