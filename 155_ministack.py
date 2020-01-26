class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []


    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1] :
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if len(self.data) > 0:
            self.helper.pop()
            return self.data.pop()

    def top(self) -> int:
        if len(self.data) > 0:
            return self.data[-1]

    def getMin(self) -> int:
        if len(self.helper) > 0:
            return self.helper[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()