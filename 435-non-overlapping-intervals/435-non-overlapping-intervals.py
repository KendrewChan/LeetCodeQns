class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1]) # Sort by when it ends
        intervals.sort(key=lambda x: x[0]) # Sort by when it starts (this has greater priority thus sorted last)
        count_stay = 0
        curr_end = 5*(10**4) # Maximum
        print(intervals)
        for i in range(len(intervals)-1, -1, -1):
            start, end = intervals[i]
            if end <= curr_end: # Check that it's within range, if not skip
                curr_end = start # We automatically choose the interval that starts the latest because of how we sorted them
                count_stay += 1
        return len(intervals) - count_stay
            