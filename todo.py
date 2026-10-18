def show_tasks(tasks):
    for i,task in enumerate(tasks,start=1):
        print(i,task)

def add_task(tasks):
    task=input("请输入要添加的任务：").strip()
    tasks.append(task)
    print("添加完成")

def delete_task(tasks):
    for i ,task in enumerate(tasks,start=1):
        print(i,task)
    index=int(input("想删除哪个:").strip())
    tasks.pop(index-1)
    print("已删除")
