# Creating a stack datatype

class Stack:

    stk = []
    top = None

    def __int__(self):
        pass

    @staticmethod
    def update_top():
        Stack.top = Stack.stk[len(Stack.stk) - 1]

    def is_empty(self) -> bool:
        return self.stk == []

    def append(self, obj) -> None:
        self.stk.append(obj)
        Stack.update_top()

    def pop(self):

        if self.is_empty():
            return "Stack underflow"

        elif not self.is_empty():
            popped = self.stk.pop()
            Stack.update_top()
            return popped
