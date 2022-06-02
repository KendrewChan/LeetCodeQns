class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        left,right = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if left <= interval[0] <= right:
                right = max(right, interval[1])
            else:
                res.append([left,right])
                left,right = interval
        res.append([left,right])
        return res
            
"""
[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
[[1,4],[0,4]]
[[1,4],[2,3]]
"""