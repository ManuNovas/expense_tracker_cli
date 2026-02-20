from os.path import exists
from json import load, dump

from src.application.ports.output import RepositoryOutputPort


class JsonOutputAdapter(RepositoryOutputPort):
    file_name: str
    data: list[dict]

    def __init__(self, file_name: str):
        self.file_name = file_name

    def open(self):
        if not exists(self.file_name):
            with open(self.file_name, "w") as file:
                file.write("[]")
        with open(self.file_name, "r") as file:
            self.data = load(file)

    def get_next_id(self):
        return self.data[-1]["id"] + 1 if len(self.data) > 0 else 1
    
    def save(self):
        with open(self.file_name, "w") as file:
            dump(self.data, file)
    
    def create(self, item: dict) -> int:
        self.open()
        item["id"] = self.get_next_id()
        self.data.append(item)
        self.save()
        return item["id"]
