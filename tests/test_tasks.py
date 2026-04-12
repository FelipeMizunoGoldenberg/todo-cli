"""
test_tasks.py - Testes automatizados para o gerenciador de tarefas.
Utiliza pytest e arquivos temporários para não poluir dados reais.
"""

import json
import os
import tempfile

import pytest

from src.task_manager import add_task, complete_task, list_tasks, remove_task


@pytest.fixture
def temp_file():
    """Fixture: cria um arquivo JSON temporário para cada teste."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as f:
        json.dump([], f)
        temp_path = f.name

    yield temp_path

    # Limpeza após o teste
    if os.path.exists(temp_path):
        os.remove(temp_path)


# ──────────────────────────────────────────────
# Testes: Adicionar Tarefa
# ──────────────────────────────────────────────

def test_add_task_successfully(temp_file):
    """Deve adicionar uma tarefa com descrição válida."""
    task = add_task("Estudar matemática", filepath=temp_file)

    assert task["id"] == 1
    assert task["description"] == "Estudar matemática"
    assert task["status"] == "pendente"


def test_add_multiple_tasks_increments_id(temp_file):
    """Deve incrementar o ID a cada nova tarefa adicionada."""
    task1 = add_task("Tarefa 1", filepath=temp_file)
    task2 = add_task("Tarefa 2", filepath=temp_file)
    task3 = add_task("Tarefa 3", filepath=temp_file)

    assert task1["id"] == 1
    assert task2["id"] == 2
    assert task3["id"] == 3


def test_add_task_empty_description_raises_error(temp_file):
    """Deve lançar ValueError ao tentar adicionar tarefa com descrição vazia."""
    with pytest.raises(ValueError, match="vazia"):
        add_task("", filepath=temp_file)


def test_add_task_whitespace_only_raises_error(temp_file):
    """Deve lançar ValueError para descrição com apenas espaços."""
    with pytest.raises(ValueError, match="vazia"):
        add_task("   ", filepath=temp_file)


# ──────────────────────────────────────────────
# Testes: Listar Tarefas
# ──────────────────────────────────────────────

def test_list_tasks_empty(temp_file):
    """Deve retornar lista vazia quando não há tarefas."""
    tasks = list_tasks(filepath=temp_file)
    assert tasks == []


def test_list_tasks_returns_all(temp_file):
    """Deve retornar todas as tarefas adicionadas."""
    add_task("Tarefa A", filepath=temp_file)
    add_task("Tarefa B", filepath=temp_file)

    tasks = list_tasks(filepath=temp_file)
    assert len(tasks) == 2
    assert tasks[0]["description"] == "Tarefa A"
    assert tasks[1]["description"] == "Tarefa B"


# ──────────────────────────────────────────────
# Testes: Remover Tarefa
# ──────────────────────────────────────────────

def test_remove_task_successfully(temp_file):
    """Deve remover uma tarefa existente pelo ID."""
    add_task("Tarefa para remover", filepath=temp_file)
    removed = remove_task(1, filepath=temp_file)

    assert removed["id"] == 1
    assert list_tasks(filepath=temp_file) == []


def test_remove_task_not_found_raises_error(temp_file):
    """Deve lançar ValueError ao tentar remover tarefa inexistente."""
    with pytest.raises(ValueError, match="não encontrada"):
        remove_task(999, filepath=temp_file)


def test_remove_task_does_not_affect_others(temp_file):
    """Remover uma tarefa não deve afetar as demais."""
    add_task("Manter esta", filepath=temp_file)
    add_task("Remover esta", filepath=temp_file)

    remove_task(2, filepath=temp_file)
    tasks = list_tasks(filepath=temp_file)

    assert len(tasks) == 1
    assert tasks[0]["id"] == 1


# ──────────────────────────────────────────────
# Testes: Marcar como Concluída
# ──────────────────────────────────────────────

def test_complete_task_successfully(temp_file):
    """Deve marcar uma tarefa existente como concluída."""
    add_task("Tarefa a concluir", filepath=temp_file)
    task = complete_task(1, filepath=temp_file)

    assert task["status"] == "concluída"


def test_complete_task_persists_status(temp_file):
    """O status 'concluída' deve ser persistido no arquivo."""
    add_task("Verificar persistência", filepath=temp_file)
    complete_task(1, filepath=temp_file)

    tasks = list_tasks(filepath=temp_file)
    assert tasks[0]["status"] == "concluída"


def test_complete_task_not_found_raises_error(temp_file):
    """Deve lançar ValueError ao tentar concluir tarefa inexistente."""
    with pytest.raises(ValueError, match="não encontrada"):
        complete_task(42, filepath=temp_file)
