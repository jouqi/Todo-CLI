from todo.py import add_task


def test_add_task_success():
    tasks = []

    add_task(tasks, "学习 Python", "high")

    assert len(tasks) == 1
    assert tasks[0]["title"] == "学习 Python"
    assert tasks[0]["done"] is False
    assert tasks[0]["priority"] == "high"


def test_add_task_empty_title():
    tasks = []

    add_task(tasks, "", "high")

    assert tasks == []


def test_add_task_invalid_priority():
    tasks = []

    add_task(tasks, "学习 Python", "abc")

    assert tasks == []