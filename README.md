# api_rest_flask

## Integrantes

- Giovane Bianchi Milani (21102209)
- Vinícius Boff (21103109)
- André Rodrigues (20280010)

## Tutorial Linux

### Instalando Libs
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Rodando local
```
flask run
```

## Tutorial Windows

### Instalando Libs
```
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### Rodando local
```
flask run
```

## Usando a API
Pode usar Postman importando a coleção no arquivo 'API-REST-FLASK.postman_collection.json' ou a documentação do Swagger em http://localhost:5000/teams

Além disso, pode-se rodar o arquivo de teste com o comando:

```
python ./client/main.py
```