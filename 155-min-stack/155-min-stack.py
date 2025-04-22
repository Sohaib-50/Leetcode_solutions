class MinStack:
    def __init__(self):
        self.minimums = []
        self.stacc = []
        

    def push(self, val: int) -> None:
        self.stacc.append(val)

        if not self.minimums:
            self.minimums.append(val)
        else:
            latest_minimum = self.getMin()
            if val < latest_minimum:
                self.minimums.append(val)
            else:
                self.minimums.append(latest_minimum)

    def pop(self) -> None:
        self.stacc.pop()
        self.minimums.pop()
        
    def top(self) -> int:
        return self.stacc[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
