# Projeto-FastAPI

Aplicação simples com backend em FastAPI e frontend em Streamlit para registrar e listar entregas usando SQLite.

## Requisitos
- Python 3.10+ (recomendado)
- pip

## Preparação (recomendada: virtual environment)
1. Abrir PowerShell na pasta do projeto:
```powershell
cd C:\Users\Acer\Desktop\Projeto-FastAPI
```
2. Criar e ativar um virtualenv (opcional, mas recomendado):
```powershell
python -m venv venv
# ativar
.\venv\Scripts\Activate.ps1
```
3. Atualizar pip e instalar dependências:
```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

## Rodando a aplicação
1. Iniciar o backend (FastAPI) em um terminal:
```powershell
python -m uvicorn api.api:app --reload --host 127.0.0.1 --port 8000
```
2. Iniciar o frontend (Streamlit) em outro terminal:
```powershell
streamlit run api/app.py
```
3. Acessar o painel Streamlit (normalmente em http://localhost:8501). O backend estará em http://127.0.0.1:8000.

## Observações e solução de problemas
- Erro `requests.exceptions.ConnectionError` no Streamlit: significa que o backend não está rodando. Verifique se o uvicorn está ativo e escutando em `127.0.0.1:8000`.
- Se receber erro ao inserir entrega (por exemplo ID duplicado), escolha outro ID ou modifique o backend para gerar IDs automaticamente.
- O banco SQLite (`entregas.db`) é criado automaticamente na raiz do projeto quando o backend inicia (caso o código que cria a tabela esteja presente).
- Se a porta 8000 estiver ocupada, altere a porta em ambos os comandos e atualize o endereço no frontend (`api/app.py`) se necessário.

## Próximos passos e melhorias
- Implementar geração automática de IDs no backend (autoincrement).
- Adicionar validações e mensagens mais detalhadas no frontend.
- Criar testes automatizados para o backend.

---
README atualizado com instruções para rodar localmente.