class MinStack(object):
    # Credits: https://leetcode.com/problems/min-stack/discuss/49010/Clean-6ms-Java-solution
    
    def __init__(self):
        self.head = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(val, self.head.currMin), self.head)

    def pop(self):
        """
        :rtype: None
        """
        self.head = self.head.nxt
        

    def top(self):
        """
        :rtype: int
        """
        return self.head.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.head.currMin
        
# LinkedList maintaining the curr minimum value
class Node(object):
    def __init__(self, val, currMin, nxt):
        self.val = val
        self.currMin = currMin
        self.nxt = nxt
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()