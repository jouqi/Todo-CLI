from todo import show_tasks,delete_task,add_task,done_task
from storage import load_tasks,save_tasks

tasks=load_tasks()
while True:
    print("\n==== Todo CLI ====")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 完成任务")
    print("5. 退出")

    try:
        choice=int(input('请选择：').strip())
        if choice>5 or choice<1:
            print("请输入正确功能号")
            continue
    except ValueError as e:
        print("请输入数字")
        continue

    if choice==1: 
        show_tasks(tasks)
    elif choice==2:
        while True:
            task_title=input("请输入要添加的任务：").strip()
            task_level=input("请输入等级：(high,medium,low)").strip()
            if add_task(tasks,task_title,task_level):
                break
    elif choice==3:
        while True:
            try:
                index=int(input("你想删除哪个:").strip())
                if delete_task(tasks,index):
                    break
            except ValueError as e:
                print("请输入数字")
                continue
    elif choice==4:
        show_tasks(tasks)
        while True:
            try:
                index=int(input("你完成了哪个:").strip())
                if done_task(tasks,index):
                    break
            except ValueError:
                print("请输入数字")
                continue
    elif choice==5:
        save_tasks(tasks)
        break

