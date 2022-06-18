class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for i in range(32): # Note how n always has 32 bits
            reverse = reverse*2 + n%2
            n //= 2
        return reverse