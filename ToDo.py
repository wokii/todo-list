import json
from uuid import uuid4


class ToDoEntry:
    def __init__(self, desc: str = None, **kwargs):
        if desc is not None:
            self.description = desc
            self.uuid = str(uuid4())
            self.done = False
        else:
            print(f"else: kwargs: {kwargs}")
            self.__dict__.update(**kwargs)


    def mark_as_done(self):
        self.done = True

    def to_dict(self):
        print("to_dict", self.__dict__)
        return self.__dict__

    def as_str(self):
        return self.description

    def uuid(self):
        return self.uuid()


class ToDoList:
    def __init__(self, todo_dict={}):
        self.todo_dict: dict[str, ToDoEntry] = todo_dict

    def add(self, new_todo: ToDoEntry):
        self.todo_dict[new_todo.uuid] = new_todo

    def mard_todo_as_done(self, uuid):
        self.todo_dict[uuid].mark_as_done()

    def delete(self, uuid):
        self.todo_dict.pop(uuid, None)

    def as_str(self):
        return ", ".join([todo_entry.description for uuid, todo_entry in self.todo_dict.items()])

    def to_json(self):
        return json.dumps({uuid: todo_entry.to_dict() for uuid, todo_entry in self.todo_dict.items()}, ensure_ascii=False)
