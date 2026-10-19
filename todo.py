def show_tasks(tasks):
    if not tasks:
        print("没有数据")
        return False
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
        return False
    if task_level in level:
        task= {'title':task_title,'done':False,'priority':task_level}
        tasks.append(task)
        print("添加完成")
        return True
    else:
        print("请从三个里选")
        return False

def done_task(tasks,index):
    if is_invalid_index(tasks,index):
        print("请输入正确任务号")
        return False
    tasks[index-1]['done']=True
    print("设置完成")
    return True


def delete_task(tasks,index):
    show_tasks(tasks)
    if is_invalid_index(tasks,index):
        print("请输入正确任务号")
        return False
    tasks.pop(index-1)
    print("已删除")
    return True

def is_invalid_index(tasks,index):
    if index>len(tasks) or index<1:
        return True
    else:
        return False
