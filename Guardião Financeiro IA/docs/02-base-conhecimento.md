# Base de Conhecimento do Agente

## Visão geral

O Guardião Financeiro IA utiliza uma base de conhecimento estruturada com dados mockados de um cliente bancário. Essa base foi criada para permitir respostas contextualizadas, seguras e coerentes com o perfil do usuário, sem depender de dados reais ou sensíveis.

A base de conhecimento combina informações financeiras, histórico de relacionamento e catálogo de produtos, permitindo ao agente atuar como um assistente de orientação financeira pessoal.

## Objetivo da base de conhecimento

A base de conhecimento tem como objetivo fornecer contexto suficiente para que o agente consiga:

- interpretar o perfil financeiro do cliente;
- analisar hábitos de consumo;
- acompanhar metas financeiras;
- recuperar interações anteriores;
- recomendar produtos compatíveis com o perfil e os objetivos do usuário;
- evitar respostas inventadas ou incompatíveis com os dados disponíveis.

## Fontes de dados utilizadas

### 1. `transacoes.csv`

Arquivo em formato CSV com o histórico simplificado de movimentações financeiras do cliente.

#### Estrutura:
- `data`
- `descricao`
- `categoria`
- `valor`
- `tipo`

#### Finalidade no agente:
- calcular total de entradas e saídas;
- identificar categorias com maior gasto;
- gerar resumos financeiros;
- detectar padrões simples de consumo;
- apoiar respostas sobre orçamento e comportamento financeiro.

#### Exemplos de uso:
- “Quanto gastei em alimentação?”
- “Qual foi meu maior gasto do mês?”
- “Estou gastando muito com transporte?”

---

### 2. `historico_atendimento.csv`

Arquivo em formato CSV com registros de interações anteriores entre o cliente e os canais de atendimento.

#### Estrutura:
- `data`
- `canal`
- `tema`
- `resumo`
- `resolvido`

#### Finalidade no agente:
- recuperar contexto de dúvidas anteriores;
- evitar repetição de orientação já fornecida;
- personalizar respostas com base no histórico do relacionamento;
- reforçar continuidade no atendimento.

#### Exemplos de uso:
- “Você já me explicou algo sobre Tesouro Selic?”
- “Eu já tive problema com o app?”
- “Quais temas eu consultei antes?”

---

### 3. `perfil_investidor.json`

Arquivo em formato JSON com os dados principais do cliente, incluindo renda, patrimônio, perfil de investidor, objetivo principal e metas.

#### Estrutura principal:
- nome
- idade
- profissão
- renda_mensal
- perfil_investidor
- objetivo_principal
- patrimonio_total
- reserva_emergencia_atual
- aceita_risco
- metas

#### Finalidade no agente:
- adaptar linguagem e recomendações ao perfil do cliente;
- avaliar compatibilidade entre produto e tolerância a risco;
- acompanhar metas financeiras;
- responder de forma personalizada e consultiva.

#### Exemplos de uso:
- “Meu perfil é conservador ou moderado?”
- “Quanto falta para minha reserva de emergência?”
- “Estou perto da minha meta do apartamento?”

---

### 4. `produtos_financeiros.json`

Arquivo em formato JSON com a lista de produtos financeiros disponíveis para recomendação.

#### Estrutura principal:
- nome
- categoria
- risco
- rentabilidade
- aporte_minimo
- indicado_para

#### Finalidade no agente:
- sugerir produtos adequados ao perfil do cliente;
- comparar alternativas de investimento;
- justificar recomendações com base em risco, liquidez e objetivo;
- restringir sugestões ao catálogo disponível no projeto.

#### Exemplos de uso:
- “Qual produto combina com meu perfil?”
- “Existe opção de baixo risco para reserva de emergência?”
- “Qual investimento exige menor aporte inicial?”

## Estratégia de uso no agente

O agente utiliza a base de conhecimento como fonte principal de contexto. Em vez de responder de forma genérica, ele consulta os arquivos disponíveis e cruza informações para gerar respostas mais úteis.

Exemplo de combinação de dados:
- `perfil_investidor.json` + `produtos_financeiros.json`: recomendação de investimentos;
- `transacoes.csv` + `perfil_investidor.json`: análise de gastos e capacidade de poupança;
- `historico_atendimento.csv` + pergunta atual: continuidade de atendimento e personalização da resposta.

## Regras de confiabilidade

Para reduzir alucinações e aumentar a segurança das respostas, o agente deve seguir estas regras:

- responder apenas com base nos dados presentes na base de conhecimento;
- informar claramente quando não houver informação suficiente;
- não inventar movimentações, metas ou produtos inexistentes;
- não recomendar produtos incompatíveis com o perfil do cliente;
- não prometer rentabilidade futura;
- priorizar explicações objetivas, claras e justificadas pelos dados.

## Limitações da base

A base de conhecimento utilizada neste projeto é mockada e simplificada. Por isso:

- representa apenas um cliente;
- não cobre cenários complexos de mercado;
- não possui atualização em tempo real;
- não substitui aconselhamento financeiro profissional;
- serve apenas como protótipo acadêmico para fins educacionais.

## Possíveis expansões futuras

Em versões futuras, a base de conhecimento pode ser ampliada com:

- múltiplos perfis de clientes;
- mais meses de transações;
- segmentação por objetivos financeiros;
- FAQ bancário;
- políticas de segurança e compliance;
- integração com banco de dados relacional ou vetorial.