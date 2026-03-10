# API Cinema - Automação de Testes

Projeto desenvolvido para automação de testes da **API Cinema**, utilizando **Playwright com Python**.  
O objetivo deste projeto é validar os principais endpoints da API responsáveis pelo gerenciamento de filmes e reservas de ingressos.

Este projeto faz parte de um **challenge de QA**, onde foi aplicado planejamento de testes, criação de cenários, automação e documentação do processo.

# Uso de Inteligência Artificial no Planejamento de Testes

Durante o planejamento do projeto foi utilizado um prompt para auxiliar na evolução do plano de testes da API Cinema.

O objetivo foi identificar possíveis melhorias na cobertura de testes, novos cenários negativos e testes de borda que poderiam aumentar a qualidade da automação.

### Prompt utilizado

"Analise o plano de testes de uma API de cinema contendo endpoints de filmes e tickets.  
Sugira melhorias na cobertura de testes, novos cenários negativos, possíveis testes de borda (boundary testing) e melhorias na estratégia de automação considerando boas práticas de testes de API."

### Resultado da análise

A análise sugeriu melhorias importantes como:

- inclusão de testes de **boundary testing**
- cenários de **concorrência na compra de tickets**
- validação de **integridade de dados**
- testes de **segurança e autorização**
- validação de **schema da resposta da API**

Essas sugestões ajudam a evoluir o plano de testes e ampliar a cobertura da automação.

---

# Objetivo do Projeto

O objetivo deste projeto é garantir o funcionamento correto da API Cinema através de testes automatizados que validam:

- criação de filmes
- listagem de filmes
- busca de filmes por ID
- atualização de filmes
- exclusão de filmes
- criação de reservas de ingressos

Também foi criado um **fluxo completo automatizado**, simulando o comportamento real de um usuário.

---

# Escopo dos Testes

Endpoints testados:

## Movies

- POST `/movies` → Criar filme
- GET `/movies` → Listar filmes
- GET `/movies/{id}` → Buscar filme por ID
- PUT `/movies/{id}` → Atualizar filme
- DELETE `/movies/{id}` → Deletar filme

## Tickets

- POST `/tickets` → Criar reserva de ingresso

---

# Fora do Escopo

Este projeto foca exclusivamente em **testes funcionais**.

Não foram incluídos:

- testes de performance
- testes de carga
- testes de segurança
- autenticação
- testes de interface gráfica

---

# Estratégia de Teste

A estratégia utilizada inclui:

- Testes automatizados com **Playwright**
- Validação de **status code**
- Validação da **estrutura da resposta JSON**
- Validação de **regras de negócio**
- Separação de responsabilidades no código
- Reutilização de dados de teste
- Execução independente dos cenários

---

# Mapa Mental

O planejamento dos testes foi realizado utilizando **mapa mental**, organizando os endpoints da API e os cenários de teste.

Estrutura:

API Cinema

Movies
- GET /movies
- GET /movies/{id}
- POST /movies
- PUT /movies/{id}
- DELETE /movies/{id}

Tickets
- POST /tickets

Também foram definidos cenários **positivos e negativos** para validação das regras de negócio.

---

# Estrutura do Projeto

API_Cinema
│
├── tests
│   ├── movies
│   │   ├── test_create_movie.py
│   │   ├── test_get_movie.py
│   │   ├── test_update_movie.py
│   │   └── test_delete_movie.py
│   │
│   ├── tickets
│   │   └── test_create_ticket.py
│   │
│   └── flows
│       └── test_full_flow.py
│
├── services
│   ├── movie_service.py
│   └── ticket_service.py
│
├── factories
│   ├── movie_factory.py
│   └── ticket_factory.py
│
├── utils
│   └── api_client.py
│
├── requirements.txt
└── README.md

---

# Pré-requisitos

Para executar o projeto é necessário ter instalado:

- Python 3.10 ou superior

- Pip

- Git

---

# Como executar o projeto

Clone o repositório:
git clone <url-do-repositorio>

Acesse a pasta do projeto:
cd API_Cinema

Instale as dependências:
pip install -r requirements.txt

Execute os testes:
pytest -v

---

# Issues Criadas

Durante a execução dos testes foram identificados possíveis bugs e melhorias na API, que foram registradas como issues no repositório.

Exemplos:

- validação de campos obrigatórios

- inconsistência em validação de dados

- melhorias no tratamento de erros

- possíveis melhorias de performance

---

# Boas Práticas Aplicadas

Durante o desenvolvimento da automação foram aplicadas boas práticas como:

- separação de responsabilidades

- reutilização de código

- organização por camadas

- cenários independentes

- uso de factories para geração de dados

- criação de fluxos completos de teste

---

# Conclusão

Este projeto demonstra a aplicação prática de planejamento de testes, automação de API e organização de código seguindo boas práticas de QA.

A automação contribui para garantir maior confiabilidade da API e facilitar a detecção precoce de falhas.
