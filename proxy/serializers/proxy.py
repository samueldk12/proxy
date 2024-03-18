from pydantic import BaseModel, root_validator

class ProxyCreateResponse(BaseModel):
    reability: float
    date_created: str
        
class ProxyCreateRequest(BaseModel):
    proxy: str
    font: str
    location: str | None 
    ssl: bool
    
class ProxyResponse(BaseModel):
    list_proxies: list[str] | None

class ProxyUpdateResponse(BaseModel):
    reability: float
    date_updated: str

class ProxyUpdateRequest(BaseModel):
    site: str
    proxy: str
    status: str
    location: str

