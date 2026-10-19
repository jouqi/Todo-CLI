from todo import add_task
from todo import done_task
from todo import delete_task


def test_add_task_success():
    tasks = []

    result=add_task(tasks, "学习 Python", "high")

    assert len(tasks) == 1
    assert tasks[0]["title"] == "学习 Python"
    assert tasks[0]["done"] is False
    assert tasks[0]["priority"] == "high"
    assert result is True


def test_add_task_empty_title():
    tasks = []

    result=add_task(tasks, "", "high")

    assert tasks == []
    assert result is False


def test_add_task_invalid_priority():
    tasks = []

    result=add_task(tasks, "学习 Python", "abc")

    assert tasks == []
    assert result is False



def test_done_task_success():
    tasks = [
        {"title": "学习 Python", "done": False, "priority": "high"}
    ]

    result=done_task(tasks, 1)

    assert tasks[0]["done"] is True
    assert result is True

def test_done_task_invalid_index_too_large():
    tasks = [
        {"title": "学习 Python", "done": False, "priority": "high"}
    ]

    result=done_task(tasks, 2)

    assert tasks[0]["done"] is False
    assert result is False

def test_done_task_invalid_index_zero():
    tasks = [
        {"title": "学习 Python", "done": False, "priority": "high"}
    ]

    result=done_task(tasks, 0)

    assert tasks[0]["done"] is False
    assert result is False


def test_delete_task_success():
    tasks = [
        {"title": "学习 Python", "done": False, "priority": "high"}
    ]
    result=delete_task(tasks,1)

    assert tasks==[]
    assert result is True

def test_delete_task_invalid_index_too_large():
    tasks = [
        {"title": "学习 Python", "done": False, "priority": "high"}
    ]
    expected = [
    {"title": "学习 Python", "done": False, "priority": "high"}
    ]
    result=delete_task(tasks,2)
    assert tasks!=[]
    assert result is False
    assert tasks==expected

def test_delete_task_invalid_index_zero():
    tasks = [
        {"title": "学习 Python", "done": False, "priority": "high"}
    ]
    expected = [
    {"title": "学习 Python", "done": False, "priority": "high"}
    ]
    result=delete_task(tasks,0)
    assert tasks!=[]
    assert result is False
    assert tasks==expected