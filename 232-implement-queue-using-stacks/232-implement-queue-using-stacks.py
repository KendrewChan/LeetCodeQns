class MyQueue(object):
    
    def __init__(self):
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Reverse & Append first (just draw it out, the pattern becomes easier)
        temp = []
        while self.stk:
            temp.append(self.stk.pop())
        temp.append(x)
        # Reverse back
        while temp:
            self.stk.append(temp.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.stk.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()