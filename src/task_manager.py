"""
task_manager.py - Lógica de negócio para gerenciamento de tarefas.
"""

from src.storage import load_tasks, save_tasks


def add_task(description: str, filepath: str = None) -> dict:
    """
    Adiciona uma nova tarefa com descrição fornecida.
    Lança ValueError se a descrição for vazia.
    """
    description = description.strip()
    if not description:
        raise ValueError("A descrição da tarefa não pode ser vazia.")

    kwargs = {"filepath": filepath} if filepath else {}
    tasks = load_tasks(**kwargs) if filepath else load_tasks()

    # Gera novo ID baseado no maior ID existente + 1
    new_id = max((t["id"] for t in tasks), default=0) + 1

    task = {
        "id": new_id,
        "description": description,
        "status": "pendente",
    }

    tasks.append(task)

    if filepath:
        save_tasks(tasks, filepath)
    else:
        save_tasks(tasks)

    return task


def list_tasks(filepath: str = None) -> list[dict]:
    """Retorna todas as tarefas salvas."""
    if filepath:
        return load_tasks(filepath)
    return load_tasks()


def remove_task(task_id: int, filepath: str = None) -> dict:
    """
    Remove uma tarefa pelo ID.
    Lança ValueError se a tarefa não for encontrada.
    """
    tasks = load_tasks(filepath) if filepath else load_tasks()
    task_to_remove = next((t for t in tasks if t["id"] == task_id), None)

    if not task_to_remove:
        raise ValueError(f"Tarefa com ID {task_id} não encontrada.")

    tasks = [t for t in tasks if t["id"] != task_id]

    if filepath:
        save_tasks(tasks, filepath)
    else:
        save_tasks(tasks)

    return task_to_remove


def complete_task(task_id: int, filepath: str = None) -> dict:
    """
    Marca uma tarefa como concluída pelo ID.
    Lança ValueError se a tarefa não for encontrada.
    """
    tasks = load_tasks(filepath) if filepath else load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "concluída"
            if filepath:
                save_tasks(tasks, filepath)
            else:
                save_tasks(tasks)
            return task

    raise ValueError(f"Tarefa com ID {task_id} não encontrada.")
