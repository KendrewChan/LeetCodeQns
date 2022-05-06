class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_curr = len(a)-1
        b_curr = len(b)-1
        carry_forward = 0
        s = ""
        while a_curr >= 0 or b_curr >= 0:
            curr = carry_forward
            # Separating a_curr and b_curr allows us to continue looping 1 when the other has no more values to be added
            if a_curr >= 0:
                curr += int(a[a_curr])
                a_curr -= 1
            if b_curr >= 0: 
                curr += int(b[b_curr])
                b_curr -= 1
            s += str(curr % 2) # if sum==2 or sum==0 append 0
            carry_forward = curr//2 # if sum==2 we have a carry, else no carry 1/2 rounds down to 0 in integer arithematic
        if carry_forward:
            s += str(carry_forward) # Add leftover carry
        return s[::-1] # Reverse to get final answer
                            
            