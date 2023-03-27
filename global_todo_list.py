import json

from ToDo import ToDoEntry, ToDoList

todo_1 = ToDoEntry("help hyf")
todo_2 = ToDoEntry("我是一个骄傲的ADHD患者")
todo_list = ToDoList()

todo_list.add(todo_1)
todo_list.add(todo_2)

is_writing = True

if is_writing:
    with open("rawData", "w") as f:
        f.write(todo_list.to_json())

else:
    with open("rawData", "r") as f:
        data = f.read()

        dict = json.loads(data)
        # convert_file.write(json.dumps(todo_list.to_json()))
