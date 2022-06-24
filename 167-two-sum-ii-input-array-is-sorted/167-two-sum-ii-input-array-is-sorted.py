class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers)-1
        while lo < hi:
            total = numbers[lo] + numbers[hi]
            if total > target:
                hi -= 1
            elif total < target:
                lo += 1
            else:
                return [lo+1, hi+1]
        return []
            