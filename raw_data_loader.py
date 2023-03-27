import json
from ToDo import ToDoEntry, ToDoList
from types import SimpleNamespace


def read_from_file(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        todo_dict = json.loads(data)

    return todo_dict


def get_todo_list_from_file(file_name):
    raw_todo_dict = read_from_file(file_name)
    print("raw_todo_dict", raw_todo_dict)
    todo_dict = {
        uuid: ToDoEntry(**entry_dict) for uuid, entry_dict in raw_todo_dict.items()
    }

    return ToDoList(todo_dict)


def write_to_file(todo_list):
    with open("rawData", "w") as f:
        print(f"writing: {todo_list.to_json()}")
        f.write(todo_list.to_json())


def write_example_raw_data():
    todo_1 = ToDoEntry("help hyf")
    todo_2 = ToDoEntry("我是一个骄傲的ADHD患者")
    todo_list = ToDoList()

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    with open("rawData", "w") as f:
        f.write(todo_list.to_json())
