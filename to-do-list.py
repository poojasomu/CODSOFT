tasks = []

while True:
    a = int(input("""
1. Add a task
2. Mark a task done
3. Show the tasks 
4. Exit
            """))
    
    if a == 1:
        b = int(input("How many tasks to be added? "))
        for i in range(b):
            task = input("Enter task: ")
            tasks.append({'task': task, 'done': False})
        print("Tasks added!")
    
    elif a == 2:
        if not tasks:
            print("No tasks to mark as done.")
        else:
            for idx, task in enumerate(tasks):
                status = 'done' if task['done'] else 'not done'
                print(f"{idx + 1}. {task['task']} - {status}")
            
            task_num = int(input("Enter the number of the task to mark as done: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]['done'] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
    
    elif a == 3:
        if not tasks:
            print("No tasks added.")
        else:
            for idx, task in enumerate(tasks):
                status = 'done' if task['done'] else 'not done'
                print(f"{idx + 1}. {task['task']} - {status}")
    
    elif a == 4:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid option. Please try again.")
