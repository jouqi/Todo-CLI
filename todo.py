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
    while True:
        try:
            index=int(input("你完成了哪个:").strip())
            if index>len(tasks) or index<1:
                print("请输入正确任务号")
                continue
            break
        except ValueError as e:
            print("请输入数字")
            continue
    tasks[index-1]['done']='True'
    print("设置完成")


def delete_task(tasks):
    show_tasks(tasks)
    while True:
        try:
            index=int(input("你想删除哪个:").strip())
            if index>len(tasks) or index<1:
                print("请输入正确任务号")
                continue
            break
        except ValueError as e:
            print("请输入数字")
            continue
    tasks.pop(index-1)
    print("已删除")
