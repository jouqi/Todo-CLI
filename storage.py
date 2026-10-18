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
    temp_path='temp.json'
    try:
        with open(temp_path,'w',encoding="UTF-8") as file:
            json.dump(tasks,file,ensure_ascii=False)
        os.replace(temp_path,'my_tasks.json')
        print("数据已保存")
        if os.path.exists(temp_path):
            os.remove(temp_path)
    except Exception as e:
        print(f"保存发生了{e}错误")
        if os.path.exists(temp_path):
            os.remove(temp_path)
