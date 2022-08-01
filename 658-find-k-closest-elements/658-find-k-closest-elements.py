class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(x-num)) # sort by abs value from x
        
        return sorted(sorted_arr[:k])