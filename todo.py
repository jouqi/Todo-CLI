def show_tasks(tasks):
    for i,task in enumerate(tasks,start=1):
        print(i,task)

def add_task(tasks):
    task_title=input("请输入要添加的任务：").strip()
    task_done=input("是否完成：(True or False)").strip()
    task= {'title':task_title,'done':task_done}
    tasks.append(task)
    print("添加完成")

def done_task(tasks):
    show_tasks(tasks)
    index=int(input("你完成了哪个:").strip())
    tasks[index-1]['done']='True'
    print("设置完成")


def delete_task(tasks):
    show_tasks(tasks)
    index=int(input("想删除哪个:").strip())
    tasks.pop(index-1)
    print("已删除")
