from fastapi import APIRouter, HTTPException, Query

from proxy.serializers.proxy import ProxyCreateRequest, ProxyCreateResponse, ProxyResponse, ProxyUpdateRequest, ProxyUpdateResponse

proxy_router = APIRouter()


@proxy_router.get('/proxy', status_code=200)
async def return_proxies(
        amount: int | None = 10, 
        location: list[str] | None = None, 
        reliability: float | None = 0.5,
        site: str | None = None,
        font: str | None = None
    ) -> ProxyResponse:
    """
    Retorna uma lista de proxies no formato string com as configurações desejadas.
    """
    ...

@proxy_router.put("/proxy-update", status_code=201)
async def update_proxy(request: ProxyUpdateRequest) -> ProxyUpdateResponse:
    """
    Atualiza as informações de proxy, com intuito de alterar a confiabilidade, de cada proxy
    """
    ...

@proxy_router.post('/proxy-create', status_code=201)
async def create_proxy(request: ProxyCreateRequest) -> ProxyCreateResponse:
    """
    Cria uma nova proxy.
    """
    ...