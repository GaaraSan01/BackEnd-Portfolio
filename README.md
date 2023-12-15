# API Rest com Painel Administrador

## Tecnologias utilizadas

- Django Rest Framework;
- Swagger;
- PostgreSQL;
- Docker.

## Como inicia-lo?

- Realize o clone do projeto </br>
``` shell
git clone https://github.com/GaaraSan01/BackEnd-Portfolio.git
```

- Inicialize a virtual env </br>
```shell
python -m venv venv
```

- Ative a virtual env </br>
 *windows*
 ``` shell
 venv\Scripts\Activate
 ```</br>
  *linux/mac* 
  ``` shell
  source venv/bin/activate
  ```
 
- Instale as dependencias do projeto </br>
``` shell
pip install -r requirements.txt
```

- Realize as migrações do projeto </br>
```shell
python manage.py migrate
```

- Inicialize o projeto </br>
```shell
python manage.py runserver
```

## Documentação

- Acesse a documentação acessando o rota ```/doc``` ou ```/redoc```.

### Nota:

_É necessários criar um Bucket (S3) na AWS e fornecer as informações necessárias como está arquivo <br/>_
'''.env.example'''

- As tecnologias pode utilizar as tecnologias docker e postgreSQL se necessário, dependendo da hospedagem que será feita o deploy.