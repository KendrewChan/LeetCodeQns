class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c != "]":
                stk.append(c)
                continue
            # Backtrack into stack
            # Get string
            curr = ""
            while stk[-1] != "[":
                curr = stk.pop() + curr
            stk.pop() # Remove "["
            
            # Get multiplier
            val = ""
            while len(stk) and "0" <= stk[-1] <= "9":
                val = stk.pop() + val
            stk.append(int(val) * curr)
        
        res = ""
        for word in stk:
            res += word
        return res
                
    
        
        
            