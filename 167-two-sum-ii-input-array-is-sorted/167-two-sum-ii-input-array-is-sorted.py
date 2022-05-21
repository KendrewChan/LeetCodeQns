class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            num = numbers[i]
            d[num] = i
            
        for i in range(len(numbers)):
            num = numbers[i]
            req = target-num
            if req in d and d[req] > i:
                return [i+1, d[req]+1]
        return []