# Projeto de Avaliação referente à Aula 1 - MBA IA IBMEC

Implementação de uma API de Lógica de Negócio, contendo os seguintes requisitos:
- README.md
- API (FastAPI)
- Validação (Pydantic)
- Testes (Pytest)
- Governança (Git)

### Regra de Negócio

Calcula o total de calorias a partir da lista de alimentos informados.

### Grupo

- Marcos Vinícius Soares
- Modestino André Rodrigues Neto
- Thiago Marques Silva

## Pré-requisitos

### Software necessário:
- Python 3.8+
- Git
- VS Code (recomendado)
- Conta no GitHub

## Setup Inicial

### 1. Clone o repositório
```bash
git clone https://github.com/mavsoares/aula-1-projeto-avaliacao.git
cd aula-1-projeto-avaliacao
```

### 2. Crie o ambiente virtual (recomendado)

#### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Verifique a instalação
```bash
python --version
git --version
pytest --version
```

## Como Executar

```bash
uvicorn src.api.main:app --reload
```

Acesse: http://localhost:8000/docs

## Exemplo de Uso

POST /calcular
```json
{
  "alimentos": [
    {"nome": "arroz", "gramas": 150},
    {"nome": "feijao", "gramas": 100},
    {"nome": "frango", "gramas": 100}
  ]
}
```

**Resposta:**
```json
{
   "total_calorias": 450
}
```

## Testes

```bash
pytest src/tests/ -v
```

