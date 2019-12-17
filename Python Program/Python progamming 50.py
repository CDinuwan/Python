#Duck Typing
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self):
        print("Spellcheck")
        print("Compiling")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=MyEditor()
    