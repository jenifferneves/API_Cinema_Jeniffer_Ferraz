# API_Cinema – Test Automation

## Descrição

Este projeto contém testes automatizados de API desenvolvidos utilizando **Python + Playwright + Pytest** para validar as rotas da API de Cinema.

Os testes cobrem as seguintes funcionalidades da API:

### Movies
- Criar filme
- Listar filmes
- Deletar filme

### Tickets
- Criar ticket
- Buscar ticket
- Deletar ticket

Também existe um **teste de fluxo completo**, que valida o caminho feliz da aplicação.

---

# Estrutura do Projeto
API_Cinema
│
├── factories
│ ├── movie_factory.py
│ └── ticket_factory.py
│
├── services
│ ├── movies_service.py
│ └── tickets_service.py
│
├── tests
│ ├── flows
│ │ └── test_full_flow.py
│ │
│ ├── movies
│ │ ├── test_create_movie.py
│ │ ├── test_delete_movie.py
│ │ └── test_get_movie.py
│ │
│ └── tickets
│ ├── test_create_ticket.py
│ ├── test_delete_ticket.py
│ └── test_get_ticket.py
│
├── utils
│ └── api_client.py
│
├── requirements.txt
├── pytest.ini

---

# Tecnologias Utilizadas

- Python
- Pytest
- Playwright
- JSON

---

# API Client

O arquivo `api_client.py` contém uma classe responsável por realizar as requisições HTTP para a API.

Ele centraliza as chamadas de:

- POST
- GET
- DELETE

Isso permite reutilizar código e manter os testes mais organizados.

Exemplo de uso:

- client.post("/movies", payload)
- client.get("/movies")
- client.delete("/tickets/{id}")

---

# Factories

As Factories são responsáveis por gerar dados válidos para os testes, evitando repetição de código.

Exemplo:

movie_factory.py → gera payload válido de filme

ticket_factory.py → gera payload válido de ticket

---

# Services

A camada de services centraliza as chamadas para cada rota da API.

Exemplo:

- movies_service.py

- tickets_service.py

Isso ajuda a manter os testes mais limpos e organizados.

---

# Teste de Fluxo Completo

O teste localizado em:
- tests/flows/test_full_flow.py

Executa o fluxo completo da aplicação:

- Criar um filme

- Buscar o filme criado

- Criar um ticket para esse filme

- Deletar o ticket criado

Esse teste valida o funcionamento integrado das rotas.

---

# Como Rodar os Testes

- pytest (em seguida colocar a rota que deseja testar, ex: tests/movies/test_create_movie.py)

---

# Observação Importante

Os testes da rota movies devem ser executados individualmente.

Exemplo:

- pytest tests/movies/test_create_movie.py
- pytest tests/movies/test_get_movie.py
- pytest tests/movies/test_delete_movie.py

Isso ocorre porque alguns testes dependem de dados criados durante a execução, o que pode causar conflitos quando todos os testes são executados juntos.

Autor: Jeniffer Ferraz
Projeto desenvolvido para prática de automação de testes de API.