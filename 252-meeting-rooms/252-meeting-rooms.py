class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x[0])
        end = 0
        for interval in intervals:
            if interval[0] < end:
                return False
            end = interval[1]
        return True