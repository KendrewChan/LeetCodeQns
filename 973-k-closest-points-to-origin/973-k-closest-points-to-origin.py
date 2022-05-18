class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda point:pow(point[0],2)+pow(point[1],2))
        return points[:k]