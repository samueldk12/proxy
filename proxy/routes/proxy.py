from fastapi import APIRouter


from proxy.app import app

proxy_app = APIRouter('/')

proxy_app.add_api_route(app)


@proxy_app.get('/proxy', status_code=200)
def return_proxies(
    amount: int = 10, 
    location: list[str] = None, 
    reliability: float = 0.5,
    site: str = None
    ) -> list[str]:
    """
    Retorna uma lista de proxies no formato string com as configurações desejadas.

    :param amount: A quantidade de proxies a serem retornados
    :type amount: int
    :param location: A localização dos proxies desejados
    :type location: list[str]
    :param reliability: A confiabilidade mínima dos proxies desejados
    :type reliability: float
    :param site: Site para qual irá fazer request
    :type site: str
    :return: Uma lista de proxies com as configurações desejadas, caso não passe parametro retorna as com maior reliability.
    :rtype: list[str]
    """
    ...

@proxy_app.put("/proxy-update", status_code=201)
def update_proxy() -> None | object:
    ...