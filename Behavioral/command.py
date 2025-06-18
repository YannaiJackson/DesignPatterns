from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Receiver
class Document:
    def __init__(self):
        self.content = ""

    def insert(self, text: str):
        self.content += text

    def delete_last(self, count: int):
        self.content = self.content[:-count]


# Concrete Command
class InsertTextCommand(Command):
    def __init__(self, doc: Document, text: str):
        self.doc = doc
        self.text = text

    def execute(self):
        self.doc.insert(self.text)

    def undo(self):
        self.doc.delete_last(len(self.text))


# Usage
if __name__ == "__main__":
    doc = Document()
    history = []
    cmd = InsertTextCommand(doc, "Hello")
    cmd.execute()
    history.append(cmd)
    print(doc.content)
    last_cmd = history.pop()
    last_cmd.undo()
    print(doc.content)
