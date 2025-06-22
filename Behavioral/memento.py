
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class TextEditor:
    def __init__(self):
        self._state = ""

    def type(self, text):
        self._state += text

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()

    def get_content(self):
        return self._state


# Usage
if __name__ == "__main__":
    editor = TextEditor()
    editor.type("Hello, ")
    snapshot = editor.save()
    editor.type("world!")
    print(editor.get_content())
    editor.restore(snapshot)
    print(editor.get_content())
