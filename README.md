# 📋 Todo CLI

> Aplicação de linha de comando para gerenciamento de tarefas do dia a dia.

---

## 📌 Descrição do Problema

Muitas pessoas têm dificuldade em organizar suas tarefas diárias, esquecem compromissos e não possuem um sistema simples para controle de atividades. Ferramentas complexas muitas vezes atrapalham mais do que ajudam.

## 💡 Solução Proposta

Uma aplicação **CLI (Command Line Interface)** leve, simples e funcional, onde o usuário pode gerenciar suas tarefas diretamente pelo terminal, sem depender de interfaces gráficas ou conexão com a internet.

---

## 👥 Público-alvo

- Estudantes que preferem o terminal
- Pessoas com rotina corrida que precisam de agilidade
- Desenvolvedores e usuários avançados que vivem no terminal

---

## ⚙️ Funcionalidades

| Comando                         | Descrição                        |
|---------------------------------|----------------------------------|
| `python app.py add "Tarefa"`    | Adiciona uma nova tarefa         |
| `python app.py list`            | Lista todas as tarefas           |
| `python app.py done <id>`       | Marca uma tarefa como concluída  |
| `python app.py remove <id>`     | Remove uma tarefa pelo ID        |
| `python app.py help`            | Exibe a ajuda                    |

---

## 🗂️ Estrutura do Projeto

```
todo-cli/
├── src/
│   ├── __init__.py
│   ├── app.py           # Interface CLI (comandos)
│   ├── task_manager.py  # Lógica de negócio
│   └── storage.py       # Persistência em JSON
├── tests/
│   ├── __init__.py
│   └── test_tasks.py    # Testes automatizados
├── .github/
│   └── workflows/
│       └── ci.yml       # Pipeline CI/CD
├── app.py               # Ponto de entrada
├── pyproject.toml       # Configuração ruff + pytest
├── requirements.txt     # Dependências
├── .gitignore
├── VERSION
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12** — linguagem principal
- **JSON** — persistência de dados
- **pytest** — testes automatizados
- **ruff** — linting e formatação
- **GitHub Actions** — integração contínua (CI)

---

## 🚀 Como Instalar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/todo-cli.git
cd todo-cli
```

### 2. Crie e ative um ambiente virtual (recomendado)

```bash
# Linux/macOS
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

```bash
# Adicionar uma tarefa
python app.py add "Estudar matemática"

# Listar todas as tarefas
python app.py list

# Marcar como concluída (substitua 1 pelo ID desejado)
python app.py done 1

# Remover uma tarefa
python app.py remove 1

# Ver ajuda
python app.py help
```

### Exemplo de saída

```
$ python app.py add "Estudar matemática"
✅ Tarefa #1 adicionada: Estudar matemática

$ python app.py add "Revisar exercícios"
✅ Tarefa #2 adicionada: Revisar exercícios

$ python app.py list

📋 Suas tarefas (2 no total):

    1. [ ] Estudar matemática  (pendente)
    2. [ ] Revisar exercícios  (pendente)

$ python app.py done 1
✅ Tarefa #1 marcada como concluída: Estudar matemática

$ python app.py remove 2
🗑️  Tarefa #2 removida: Revisar exercícios
```

---

## 🧪 Como Rodar os Testes

```bash
pytest tests/ -v
```

Saída esperada:

```
tests/test_tasks.py::test_add_task_successfully PASSED
tests/test_tasks.py::test_add_multiple_tasks_increments_id PASSED
tests/test_tasks.py::test_add_task_empty_description_raises_error PASSED
...
```

---

## 🧹 Como Rodar o Lint

```bash
ruff check .
```

Para corrigir automaticamente problemas simples:

```bash
ruff check . --fix
```

---

## 🔢 Versão

```
1.0.0
```

---

## 👤 Autor

Desenvolvido como projeto acadêmico para a disciplina de **Engenharia de Software**.

---

## 📄 Licença

Este projeto é de uso acadêmico livre.
