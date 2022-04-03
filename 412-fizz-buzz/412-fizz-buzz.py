class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1,n+1):
            output = ""
            output += "Fizz" if i % 3 == 0 else ""
            output += "Buzz" if i % 5 == 0 else ""
            arr.append(str(i) if output == "" else output)
        return arr