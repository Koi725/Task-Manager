# actions.py

from utils import read_data, write_data


def add_task(title):
    data = read_data()
    tasks = data.get("tasks", [])
    new_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
    data["tasks"] = tasks
    write_data(data)


def show_tasks():
    data = read_data()
    tasks = data.get("tasks", [])
    for t in tasks:
        status = "✅" if t.get("done", False) else "❌"
        print(f"{t['id']}. {t['title']} - {status}")


def delete_task(task_id):
    data = read_data()
    tasks = [t for t in data.get("tasks", []) if t["id"] != task_id]
    data["tasks"] = tasks
    write_data(data)


def mark_done(task_id):
    data = read_data()
    for t in data.get("tasks", []):
        if t["id"] == task_id:
            t["done"] = True
    write_data(data)
