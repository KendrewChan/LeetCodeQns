class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curr = newInterval
        for interval in intervals:
            # Not within range (before)
            if interval[1] < curr[0]:
                res.append(interval)
            # Out of newInterval range (after) -> append
            elif interval[0] > curr[1]:
                res.append(curr)
                curr = interval
            # Within newInterval range -> merge
            else:
                curr[0] = min(curr[0], interval[0])
                curr[1] = max(curr[1], interval[1])
        res.append(curr)
        return res