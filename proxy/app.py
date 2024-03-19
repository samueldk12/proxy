from fastapi import FastAPI

from proxy.routes.proxy import proxy_router

app = FastAPI(
    title="Proxy API",
    description="Api para retorno de proxies gratis disponíveis.",
    version="0.1.0"
)

app.include_router(proxy_router)