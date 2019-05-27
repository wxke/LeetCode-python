最小栈
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # self.min1 = sys.maxsize
        self.res = []

    def push(self, x: int) -> None:
        self.res.append(x)
        

    def pop(self) -> None:
        self.res.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:

        return min(self.res)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
