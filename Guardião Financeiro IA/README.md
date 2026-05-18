# Guardião Financeiro IA

## Sobre o projeto

O Guardião Financeiro IA é um assistente virtual financeiro educacional desenvolvido para responder perguntas sobre gastos, metas financeiras, histórico de atendimento e sugestões de produtos com base em dados estruturados do cliente.

O projeto foi criado como protótipo prático para demonstrar a aplicação de agentes de IA em um contexto de atendimento financeiro personalizado.

## Problema

Muitos usuários possuem acesso a dados financeiros, mas não conseguem transformar essas informações em decisões práticas. O projeto busca mostrar como um agente pode organizar dados dispersos e gerar respostas mais claras, úteis e contextualizadas.

## Solução

O Guardião Financeiro IA utiliza uma base de conhecimento composta por:
- transações financeiras;
- histórico de atendimento;
- perfil do investidor;
- catálogo de produtos financeiros.

A partir desses dados, o agente consegue:
- calcular saldo e gastos por categoria;
- acompanhar metas financeiras;
- recuperar histórico de interações;
- sugerir produtos compatíveis com o perfil do cliente.

## Demonstração

![Interface do Guardião Financeiro IA](assets/tela-app.png)

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- JSON
- CSV

## Estrutura do projeto

```text
guardiao-financeiro-ia/
├── data/
├── docs/
├── src/
├── assets/
├── README.md
├── requirements.txt
└── .gitignore
```

## Como executar

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd guardiao-financeiro-ia
```

### 2. Instale as dependências
No Windows PowerShell:
```powershell
py -m pip install -r requirements.txt
```

### 3. Execute a aplicação
```powershell
py -m streamlit run src/app.py
```

## Exemplos de perguntas

Você pode testar perguntas como:
- Qual meu saldo?
- Quanto gastei com alimentação?
- Qual foi meu maior gasto?
- Quanto falta para minha reserva de emergência?
- Qual investimento combina comigo?
- Mostre meu histórico de atendimento.

## Funcionalidades atuais

- Exibição do perfil do cliente
- Resumo financeiro com entradas, saídas e saldo
- Gráfico de gastos por categoria
- Perguntas rápidas
- Chat com respostas baseadas nos dados
- Recomendações iniciais de produtos financeiros

## Documentação

A documentação do projeto está organizada na pasta `docs/`:

- `01-documentacao-agente.md`
- `02-base-conhecimento.md`
- `03-prompts.md`
- `04-metricas.md`
- `05-pitch.md`

## Segurança e limites

O agente responde apenas com base nos dados presentes no projeto.  
Ele não inventa transações, metas ou produtos, e não substitui orientação financeira profissional.

## Melhorias futuras

- Integração com LLM
- Memória conversacional mais avançada
- Mais intenções de perguntas
- Avaliação automatizada
- Suporte a múltiplos clientes

## Autor

Matheus Castro