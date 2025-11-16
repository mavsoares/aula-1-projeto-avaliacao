# Projeto de Avaliação referente à Aula 1 - MBA IA IBMEC

O projeto consiste na elaboração de uma API de Lógica de Negócio, contendo os seguintes requisitos:
- README.md
- API (FastAPI)
- Validação (Pydantic)
- Testes (Pytest)
- Governança (Git)

### Grupo

- Marcos Vinícius Soares
- Modestino André Rodrigues Neto
- Thiago Marques Silva

## O que é o projeto

Implementação da API que recebe informações de alimentos consumidos e retorna o total de calorias.

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

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Verifique a instalação
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
    {"nome": "frango", "gramas": 100},
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

