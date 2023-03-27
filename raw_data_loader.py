import json
from ToDo import ToDoEntry, ToDoList


def read_from_file(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        todo_dict = json.loads(data)

    return todo_dict


def get_todo_list_from_file(file_name):
    raw_todo_dict = read_from_file(file_name)
    todo_dict = {
        uuid: ToDoEntry(**entry_dict) for uuid, entry_dict in raw_todo_dict.items()
    }

    return ToDoList(todo_dict)


def write_to_file(todo_list):
    with open("rawData", "w") as f:
        f.write(todo_list.to_json())


def write_example_raw_data():
    todo_1 = ToDoEntry("help hyf")
    todo_2 = ToDoEntry("我是一个骄傲的ADHD患者")
    todo_list = ToDoList()

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    with open("rawData", "w") as f:
        f.write(todo_list.to_json())
