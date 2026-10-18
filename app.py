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
        if choice>5 or choice<0:
            print("请输入正确功能号")
            continue
    except ValueError as e:
        print("请输入数字")
        continue

    if choice==1: 
        show_tasks(tasks)
    elif choice==2:
        add_task(tasks)
    elif choice==3:
        delete_task(tasks)
    elif choice==4:
        done_task(tasks)
    elif choice==5:
        save_tasks(tasks)
        break

