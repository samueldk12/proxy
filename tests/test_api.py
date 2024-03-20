from fastapi.testclient import TestClient

from proxy.main import app 

client = TestClient(app)

def test_read_proxies():
    response = client.get('/proxy')
    value_response = response.json()
    assert response.status_code == 200, "Retorno não esperado ao buscar proxy"
    assert 'list_proxies' in value_response, "Chave esperada no retorno não encontrada"
    assert len(value_response['list_proxies']) == 3, "Valor correspondente menos que o minimo de proxies esperados"

def test_create_proxy():
    json = {
        "proxy": "127.0.0.1",
        "font": "www.teste.com.br",
        "location": "Brazil",
        "ssl": False      
    }
    response = client.post('/proxy', json=json)
    print(response)
    assert response.status_code == 201

def test_update_proxy():
    json = {
        "proxy": "127.0.0.1",
        "site": "www.teste.com.br",
        "location": "Brazil",
        "status": 200      
    }
    response = client.put('/proxy', json=json)
    print(response)
    assert response.status_code == 201