# load_tasks()
# save_tasks(tasks)

import json
import os

def load_tasks():
    if os.path.exists("my_tasks.json"):
        try:
            with open("my_tasks.json",'r',encoding='UTF-8') as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []
    else:
        return []

def save_tasks(tasks):
    with open("my_tasks.json",'w',encoding="UTF-8") as file:
        json.dump(tasks,file,ensure_ascii=False)