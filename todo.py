def show_tasks(tasks):
    if not tasks:
        print("没有数据")
        return
    for index,task in enumerate(tasks,start=1):
        title=task['title']
        done=task['done']
        priority=task['priority']
        if done:
            print(f"{index} [X] [{priority}] {title}")
        else:
            print(f"{index} [ ] [{priority}] {title}")
def add_task(tasks,task_title,task_level):
    level=['high','medium','low']
    if not task_title:
        print("请输入内容")
        return 
    if task_level in level:
        task= {'title':task_title,'done':False,'priority':task_level}
        tasks.append(task)
        print("添加完成")
        return 1
    else:
        print("请从三个里选")
        return

def done_task(tasks):
    if not tasks:
        print("没有数据")
        return
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
    tasks[index-1]['done']=True
    print("设置完成")


def delete_task(tasks):
    if not tasks:
        print("没有数据")
        return 
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
