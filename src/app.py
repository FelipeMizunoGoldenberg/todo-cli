"""
app.py - Ponto de entrada da aplicação CLI de controle de tarefas.

Uso:
    python app.py add "Descrição da tarefa"
    python app.py list
    python app.py remove <id>
    python app.py done <id>
"""

import sys

from src.task_manager import add_task, complete_task, list_tasks, remove_task

# Símbolos visuais para status
STATUS_ICON = {
    "pendente": "[ ]",
    "concluída": "[✓]",
}


def cmd_add(args: list[str]) -> None:
    """Comando: adicionar nova tarefa."""
    if not args:
        print("Erro: informe a descrição da tarefa.")
        print('  Exemplo: python app.py add "Estudar matemática"')
        sys.exit(1)

    description = " ".join(args)
    try:
        task = add_task(description)
        print(f"✅ Tarefa #{task['id']} adicionada: {task['description']}")
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)


def cmd_list() -> None:
    """Comando: listar todas as tarefas."""
    tasks = list_tasks()

    if not tasks:
        print("📭 Nenhuma tarefa encontrada. Adicione uma com 'add'.")
        return

    print(f"\n📋 Suas tarefas ({len(tasks)} no total):\n")
    for task in tasks:
        icon = STATUS_ICON.get(task["status"], "[ ]")
        print(f"  {task['id']:>3}. {icon} {task['description']}  ({task['status']})")
    print()


def cmd_remove(args: list[str]) -> None:
    """Comando: remover tarefa por ID."""
    if not args or not args[0].isdigit():
        print("Erro: informe o ID numérico da tarefa.")
        print("  Exemplo: python app.py remove 1")
        sys.exit(1)

    task_id = int(args[0])
    try:
        task = remove_task(task_id)
        print(f"🗑️  Tarefa #{task['id']} removida: {task['description']}")
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)


def cmd_done(args: list[str]) -> None:
    """Comando: marcar tarefa como concluída por ID."""
    if not args or not args[0].isdigit():
        print("Erro: informe o ID numérico da tarefa.")
        print("  Exemplo: python app.py done 1")
        sys.exit(1)

    task_id = int(args[0])
    try:
        task = complete_task(task_id)
        print(f"✅ Tarefa #{task['id']} marcada como concluída: {task['description']}")
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)


def show_help() -> None:
    """Exibe mensagem de ajuda com os comandos disponíveis."""
    print("""
📌 Todo CLI - Gerenciador de Tarefas

Uso:
  python app.py <comando> [argumentos]

Comandos disponíveis:
  add <descrição>   Adiciona uma nova tarefa
  list              Lista todas as tarefas
  remove <id>       Remove uma tarefa pelo ID
  done <id>         Marca uma tarefa como concluída
  help              Exibe esta ajuda

Exemplos:
  python app.py add "Estudar matemática"
  python app.py list
  python app.py done 1
  python app.py remove 1
""")


# Mapeamento de comandos para funções
COMMANDS = {
    "add": lambda args: cmd_add(args),
    "list": lambda _: cmd_list(),
    "remove": lambda args: cmd_remove(args),
    "done": lambda args: cmd_done(args),
    "help": lambda _: show_help(),
}


def main() -> None:
    """Função principal: interpreta os argumentos e executa o comando."""
    args = sys.argv[1:]

    if not args:
        show_help()
        sys.exit(0)

    command = args[0].lower()
    rest = args[1:]

    if command not in COMMANDS:
        print(f"Erro: comando '{command}' não reconhecido.")
        print("  Use 'python app.py help' para ver os comandos disponíveis.")
        sys.exit(1)

    COMMANDS[command](rest)


if __name__ == "__main__":
    main()
