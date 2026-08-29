# Radar de Estágios em TI

Sistema para organizar, filtrar e consultar oportunidades de estágio em TI. Criado como projeto de portfólio durante a graduação em Análise e Desenvolvimento de Sistemas, com o objetivo de aplicar na prática conceitos de modelagem de banco de dados relacional, backend em Python e versionamento com Git.

O projeto parte de uma lista de vagas coletadas manualmente e transforma esses dados em um banco de dados consultável através de uma API própria, com filtros por área, prazo de inscrição e modelo de trabalho.

## Tecnologias

- Python 3
- SQLite
- FastAPI + Uvicorn
- Git / GitHub
- Power BI (dashboard, em construção)

## Arquitetura

O fluxo de dados segue este caminho:

```
Planilha (Excel) → CSV (empresa.csv, vaga.csv) → script de carga (carregar_dados.py)
→ banco de dados SQLite (estagios.db) → funções de consulta (consultas.py)
→ API REST (api.py, FastAPI) → dashboard (Power BI)
```

O banco é composto por duas tabelas relacionadas:

- **empresa** (`emp_id`, `emp_nome`)
- **vaga** (`vaga_id`, `emp_id` como chave estrangeira, `vaga_area`, `vaga_prazo_final`, `vaga_link`, `vaga_modelo_trabalho`)

Separar empresa e vaga evita duplicação e inconsistência de nomes de empresas que aparecem em múltiplas vagas.

## Como rodar o projeto

```bash
git clone https://github.com/iangoor/Radar-Estagios-TI.git
cd Radar-Estagios-TI

python -m venv venv
venv\Scripts\Activate.ps1        # Windows (PowerShell)

pip install -r requirements.txt

python criar_banco.py            # cria o banco e as tabelas
python carregar_dados.py         # carrega os dados dos CSVs no banco

uvicorn api:app --reload         # inicia a API em http://127.0.0.1:8000
```

## Endpoints da API

### `GET /vagas`

Retorna vagas do banco de dados, com filtros opcionais combináveis via query string.

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `area` | texto | Filtra por área (`dev`, `dados`, `cyber`, `suporte`, `ti`) |
| `prazo` | texto (`AAAA-MM-DD`) | Retorna vagas com prazo final até a data informada, excluindo vagas sem prazo definido |
| `sem_prazo` | booleano | Se `true`, retorna apenas vagas sem prazo de inscrição informado |

**Exemplos:**
```
GET /vagas?area=cyber
GET /vagas?prazo=2026-09-01
GET /vagas?area=dados&sem_prazo=true
```

**Exemplo de resposta:**
```json
[
  {
    "vaga_id": 33,
    "vaga_area": "cyber",
    "vaga_prazo_final": "2026-08-31",
    "vaga_link": "https://secureway.gupy.io/jobs/11375178",
    "vaga_modelo_trabalho": "não informado",
    "emp_id": 28
  }
]
```

> Observação: `prazo` e `sem_prazo` são mutuamente exclusivos — não faz sentido pedir "prazo até uma data" e "sem prazo" ao mesmo tempo, então o filtro de prazo tem prioridade se os dois forem enviados juntos.


## Melhorias futuras

- Migrar de SQLite para PostgreSQL para simular um ambiente mais próximo de produção
- Adicionar coluna e endpoint de status de candidatura (aplicado, entrevista, rejeitado)
- Automatizar a coleta de novas vagas em vez de preenchimento manual
- Adicionar testes automatizados para as funções de consulta
- Deploy da API em um serviço gratuito (Render, Railway) para acesso público
