class MinStack:

    def __init__(self):
        self.stack = []
        self.minsofar = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minsofar:
            prev = self.minsofar[-1]
            curr = min(prev, val)
            self.minsofar.append(curr)
        else:
            self.minsofar.append(val)

    def pop(self) -> None:

        self.stack.pop()
        self.minsofar.pop()
        

    def top(self) -> int:

        return self.stack[-1] if self.stack else - 1
        

    def getMin(self) -> int:

        return self.minsofar[-1] if self.minsofar else -1
        
