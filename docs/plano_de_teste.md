	Plano de Testes – API Cinema
	1. Objetivo
	Este documento tem como objetivo descrever o planejamento de testes funcionais da API Cinema, responsável pelo gerenciamento de filmes e reservas de ingressos.
	O foco da automação será validar os requisitos funcionais descritos nas histórias de usuário fornecidas.
	
	2. Escopo
	Serão testados os seguintes endpoints:
	Movies
		• POST /movies
		• GET /movies
		• GET /movies/{id}
		• PUT /movies/{id}
		• DELETE /movies/{id}
	Tickets
		• POST /tickets
	
	3. Fora do Escopo
		• Testes de performance
		• Testes de carga
		• Testes de segurança
		• Testes de autenticação
		• Testes de interface gráfica
	Observação: Embora existam requisitos não funcionais de performance nas histórias, este projeto está focado exclusivamente na validação funcional.
	
	4. Estratégia de Teste
	A estratégia adotada será:
		• Testes automatizados utilizando Playwright (API Testing)
		• Validação de status code
		• Validação da estrutura do JSON
		• Validação de regras de negócio
		• Execução independente dos cenários
		• Separação de responsabilidades (ServiceObjects)
	
	5. Cenários de Teste
	
	Gerenciamento de Filmes
	
	Criar Filme (POST /movies)
	Cenários Positivos
		• Criar filme com todos os campos válidos
		• Validar retorno 201 Created
		• Validar geração de ID
		
	Cenários Negativos
		• Criar filme sem título
		• Criar filme com título duplicado
		• Criar filme com campo obrigatório vazio
	
	Listar Filmes (GET /movies)
		• Retornar lista de filmes cadastrados
		• Validar que o retorno é um array
		• Validar estrutura dos campos
	
	Buscar Filme por ID (GET /movies/{id})
		• Buscar filme existente → 200 OK
		• Buscar filme inexistente → 404 Not Found
	
	Atualizar Filme (PUT /movies/{id})
		• Atualizar filme existente → 200 OK
		• Atualizar filme inexistente → 404 Not Found
		• Atualizar com dados inválidos → erro esperado
	
	Deletar Filme (DELETE /movies/{id})
		• Deletar filme existente → 204 No Content
		• Deletar filme inexistente → 404 Not Found
	
	Reservando Ingressos
	
	Criar Reserva (POST /tickets)
	Cenários Positivos
		• Criar reserva válida → 201 Created
		
	Cenários Negativos
		• Criar reserva com seatNumber maior que 99
		• Criar reserva com price maior que 60
		• Criar reserva sem campos obrigatórios
		• Criar reserva com movieId inexistente
	
	6. Critérios de Aceite
		• Todos os cenários positivos devem retornar status esperado.
		• Cenários negativos devem retornar erros apropriados.
		• Nenhum teste deve depender de outro.
		• A execução completa da suíte deve ocorrer sem falhas inesperadas.
	
	7. Riscos Identificados
		• Falta de validação de unicidade de título.
		• Falta de validação de limites de preço ou assento.
		• Ausência de autenticação pode permitir alterações indevidas.
	
	8. Ferramentas Utilizadas
		• Node.js
		• Playwright
		• GitHub
		• API NestJS Cinema
