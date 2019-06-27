to_do = []

user_input = ""

while user_input != "q":

    if user_input == "1":
        title = input("Enter title: ")
        priority = input("Enter high, medium, or low: ")
        
        my_tasks = {
        "title": title,
        "priority": priority
        }

        to_do.append(my_tasks)
        print(to_do)

    elif user_input == "3":

        for index in range(0, len(to_do)):
            result = to_do[index]
            print(f"{index +1} - {result['title']} - {result['priority']}")
    
    elif user_input == "2":

        for index in range(0, len(to_do)):
            result = to_do[index]
            print(f"{index +1} - {result['title']} - {result['priority']}")
        
        delete_task = int(input("Enter the number of the task you would like to delete: "))
        
        def task_to_delete():
            del to_do[delete_task -1]
        
        task_to_delete()

    user_input = input("Press 1 to add a task, press 2 to delete a task, press 3 to view all tasks, and press q to quit! ")