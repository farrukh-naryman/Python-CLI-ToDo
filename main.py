from app.tasks import add_task, show_tasks, delete_task, complete_task, edit_task, show_statistics

app = True

tasks_list = [
    "╭──────────────────────────────╮",
    "│          TO-DO LIST          │",
    "│      Manage your tasks       │",
    "╰──────────────────────────────╯",
    "1. Add Task",
    "2. Show Tasks",
    "3. Delete Task",
    "4. Edit Task",
    "5. Complete/Restore Task",
    "6. Show Statistics",
    "0. Exit"]

while app:
    for i in tasks_list:
        print(i)

    try:
        choose = int(input("Choose an option:"))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choose == 1:
        add_task()
    elif choose == 2:
        show_tasks()
    elif choose == 3:
        delete_task()
    elif choose == 4:
        edit_task()
    elif choose == 5:
        complete_task()
    elif choose == 6:
        show_statistics()
    elif choose == 0:
        print("App Stopped!")
        app = False
    else:
        print("invalid option. Please choose from 0 to 6.")