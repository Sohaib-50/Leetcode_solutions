class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.popped = set()

    def popSmallest(self) -> int:
        smallest = self.smallest
        self.smallest += 1
        while self.smallest in self.popped:
            self.smallest += 1
            
        self.popped.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.popped.remove(num)
            if num < self.smallest:
                self.smallest = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
