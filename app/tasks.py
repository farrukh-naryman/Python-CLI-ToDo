tasks = []
next_id = len(tasks) + 1
completed = "Completed"
in_progress = "In Progress"

# 1 task
def add_task():
    global next_id

    task_name = input("Type task name:")
    if task_name:
        tasks.append({
            "id": next_id,
            "task": task_name,
            "status": in_progress
        })
        print("Task is added!")
        next_id += 1
    else:
        print("Task name cannot be empty!")

# 2 task
def show_tasks():
    if tasks:
        for i in tasks:
            print("ID:",i["id"],"|","Task:",i["task"],"|","Status:",i["status"])
    else:
        print("There is no task")

# 3 task
def delete_task():
    global next_id
    task_to_delete = None

    found = False
    if tasks:
        show_tasks()
        try:
            task_id = int(input("Choose task by ID:"))
        except ValueError:
            print("Please enter a valid ID!")
            return

        for i in tasks:
            if i["id"] == task_id:
                task_to_delete = i
                found = True
        if found:
            tasks.remove(task_to_delete)
            for i in range(len(tasks)):
                tasks[i]["id"] = i + 1
            next_id = len(tasks) + 1
            print("Task is deleted!")
        else:
            print("Task not found")
        show_tasks()
    else:
        print("There is no task")

# 4 task
def edit_task():
    found = False
    if tasks:
        show_tasks()
        try:
            task_id = int(input("Choose task by ID:"))
        except ValueError:
            print("Please enter a valid ID!")
            return

        for i in tasks:
            if i["id"] == task_id:
                task_title = input("Type new title for task:")
                if task_title:
                    i["task"] = task_title
                    print("Task edited!")
                    found = True
                else:
                    print("Task name cannot be empty!")
                    found = True
        if not found:
            print("Task not found!")
    else:
        print("There is no task")

# 5 task
def complete_task():
    found = False

    if tasks:
        show_tasks()
        try:
            task_id = int(input("Choose task by ID:"))
        except ValueError:
            print("Please enter a valid ID!")
            return

        for i in tasks:
            if i["id"] == task_id:
                found = True

                if i["status"] == completed:
                    print("Task is already completed.")
                    answer = input("Do you want to return it to In Progress? (y/n): ")

                    if answer.lower() == "y":
                        i["status"] = in_progress
                        print("Task returned to In Progress!")
                    elif answer.lower() == "n":
                        print("Task status was not changed.")
                    else:
                        print("Invalid choice!")

                else:
                    i["status"] = completed
                    print("Task completed!")
        if not found:
            print("Task not found!")
        show_tasks()
    else:
        print("There is no task")

# 6 task
def show_statistics():
    tasks_count = len(tasks)
    done_tasks = 0
    not_done_tasks = 0

    if tasks:
        for i in tasks:
            if i["status"] == completed:
                done_tasks +=1
            else:
                not_done_tasks += 1
        print(f"Tasks count: {tasks_count}")
        print(f"Done tasks count: {done_tasks}")
        print(f"Not done tasks count: {not_done_tasks}")
    else:
        print("There is no task")