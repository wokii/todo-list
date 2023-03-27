import json

from flask import Flask, request
from ToDo import ToDoList, ToDoEntry
from raw_data_loader import (
    get_todo_list_from_file,
    write_to_file,
    write_example_raw_data,
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    todo_list = get_todo_list_from_file("rawData")

    return todo_list.to_json()


@app.route("/add", methods=["POST"])
def add():
    try:
        todo_list = get_todo_list_from_file("rawData")
        todo_desc = request.form.get("desc", "")

        new_todo_entry = ToDoEntry(todo_desc)
        todo_list.add(new_todo_entry)

        write_to_file(todo_list)
        return_msg = json.dumps(new_todo_entry.to_dict(), ensure_ascii=False)
        return return_msg
    except Exception as e:
        return json.dumps({"error": "failed to add"})


@app.route("/reset")
def reset():
    write_example_raw_data()
    return json.dumps({"result": "succ"})
