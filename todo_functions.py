import csv

def add_todo(file_name):
    print("Add todo")
    todo_name = input("Input a todo: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("Remove todo")
    todo_name = input("Enter todo to be removed: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in f:
            if (todo_name != row[0]):
                todo_lists.append(row)
    print(todo_lists)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def mark_todo(file_name):
    print("Mark todo")
    todo_name = input("Enter todo name you would like to complete: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if(todo_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def view_todo(file_name):
    print("View todo")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # row = ["Todo 1", "False"]
            if (row[1] == "True"):
                print(f"Todo {row[0]} is complete")
            else:
                print(f"Todo {row[0]} is not complete")