"""
storage.py - Responsável pela leitura e escrita das tarefas no arquivo JSON.
"""

import json
import os

# Caminho padrão do arquivo de dados
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "tasks.json")


def load_tasks(filepath: str = DATA_FILE) -> list[dict]:
    """Carrega as tarefas do arquivo JSON. Retorna lista vazia se não existir."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks: list[dict], filepath: str = DATA_FILE) -> None:
    """Salva a lista de tarefas no arquivo JSON."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
