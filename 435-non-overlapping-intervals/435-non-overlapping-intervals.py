class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])
        count_stay = 0
        curr_end = 5*(10**4)
        for i in range(len(intervals)-1, -1, -1):
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= curr_end and end <= curr_end:
                curr_end = start
                count_stay += 1
        return len(intervals) - count_stay
            