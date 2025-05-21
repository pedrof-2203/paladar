# Paladar - Sistema de Recomendação de Restaurantes

## 1. Introdução
Paladar é um sistema inteligente de recomendação de restaurantes, baseado em filtragem colaborativa e utilizando um banco de dados gráfico. O algoritmo analisa padrões de preferência entre os usuários para sugerir estabelecimentos com maior probabilidade de agradar a cada indivíduo.

## 2. Funcionamento do Sistema

### 2.1. Fluxo Principal
- **Entrada:** O usuário insere seu primeiro nome em um campo de texto. Esse nome é enviado via método POST ao endpoint `/recommend`. Caso o nome informado não tenha correspondência no banco de dados, uma mensagem de alerta é exibida.
- **Recepção e Processamento da Requisição:** O backend recebe o nome e acessa o banco de dados gráfico por meio da classe `RestaurantRecommenderDB`.
- **Execução do Algoritmo de Recomendação:** O sistema verifica os restaurantes curtidos pelo usuário e identifica outros usuários com gostos semelhantes. A partir disso, recomenda restaurantes curtidos por esses usuários semelhantes, mas ainda não descobertos pelo usuário original.
- **Retorno ao Frontend:** A lista de recomendações é enviada ao frontend e exibida por meio do template engine Jinja. Caso não haja recomendações possíveis, uma mensagem informativa é apresentada.

### 2.2. Mecanismo de Recomendação
O banco de dados é estruturado com as entidades USUÁRIO e RESTAURANTE. Cada usuário mantém relacionamentos do tipo "LIKES" com os restaurantes que aprecia. O algoritmo analisa essas conexões para gerar recomendações com base nos usuários mais similares.

## 3. Estrutura de Dados

### 3.1. Modelagem no Neo4j
**Nós:**
- Usuário: nome, idade, gênero
- Restaurante: nome, tipo de cozinha, faixa de preço

**Relacionamentos:**
- "LIKES": Representa que um usuário gosta de determinado restaurante.

### 3.2. Lógica de Armazenamento
As relações “LIKES” são representadas como conexões diretas no grafo, sem a necessidade de tabelas auxiliares. O modelo gráfico permite capturar naturalmente as interações entre os elementos.

## 4. Características Técnicas

### 4.1. Tecnologias Utilizadas
- Neo4j: Banco de dados orientado a grafos para armazenar e consultar as relações.
- Python 3: Implementação da lógica de negócios e dos algoritmos de recomendação.
- FastAPI: Framework para construção e exposição da API.
- Jinja2: Motor de templates utilizado na renderização da interface web.

### 4.2. Vantagens da Arquitetura
- Consultas eficientes para encontrar usuários com gostos similares
- Escalabilidade para incorporar novos critérios de recomendação
- Flexibilidade para adicionar novos tipos de relacionamentos no futuro

## 5. Roadmap de Evolução

### 5.1. Melhorias Planejadas
- Sistema de avaliação com notas de 1 a 5 estrelas
- Filtros por localização geográfica e tipo de cozinha
- Integração com redes sociais para enriquecimento do perfil do usuário

## 6. Considerações Finais
O Paladar representa uma solução moderna e eficiente para recomendação personalizada de restaurantes. Combinando filtragem colaborativa e a flexibilidade dos bancos de dados em grafos, o sistema entrega sugestões relevantes e está preparado para evoluções futuras com mínima reestruturação.
