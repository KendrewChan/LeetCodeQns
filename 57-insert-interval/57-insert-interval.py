class Solution(object):
    def insert(self, intervals, newInterval):
        temp = []
        seg = newInterval
        for curr in intervals:
            if seg[1] < curr[0]: # Append the merged combinations
                temp.append(seg)
                seg = curr # This forever leads us back into the 1st condition, since the intervals were sorted in the first place
            elif seg[0] > curr[1]: # Not within range
                temp.append(curr) 
            else: # Merge
                seg[0] = min(seg[0], curr[0])
                seg[1] = max(seg[1], curr[1])
        temp.append(seg)
        return temp
# []
# [5,7]
# [[1,3],[6,9]]
# [2,5]
# [[1,2],[3,5],[6,7],[8,10],[12,16]]
# [4,8]
# [[1,5]]
# [2,3]