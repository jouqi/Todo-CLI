''' 查看任务
添加任务
删除任务
退出'''

tasks=[]
while True:
    print("\n==== Todo CLI ====")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")

    choice=int(input('请选择：').strip())
    if choice==1: 
        for i,task in enumerate(tasks,start=1):
            print(i,task)

    elif choice==2:
        task=input("请输入任务:").strip()
        tasks.append(task)
        print("添加成功")

    elif choice==3:
        for i, task in enumerate(tasks,start=1):
            print(i,task)

        index=int(input("想删除哪个：").strip())
        tasks.pop(index-1)
    elif choice==4:
        break