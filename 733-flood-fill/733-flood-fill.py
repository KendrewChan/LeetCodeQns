class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.helper(image,sr,sc,newColor,image[sr][sc])
        return image
        
    def helper(self, image, sr, sc, newColor, startingColor):
        if ((sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image[0]))) or image[sr][sc] != startingColor or image[sr][sc] == newColor:
            return
        image[sr][sc] = newColor;
        self.helper(image,sr-1,sc,newColor,startingColor)
        self.helper(image,sr,sc-1,newColor,startingColor)
        self.helper(image,sr+1,sc,newColor,startingColor)
        self.helper(image,sr,sc+1,newColor,startingColor)