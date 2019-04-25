图像渲染
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        def dp(i,j):
            image[i][j] = -1
            while i-1 >=0 and image[i-1][j] == color:
                dp(i-1,j)
            while i+1 <len(image) and image[i+1][j] == color:
                dp(i+1,j)
            while j-1 >=0 and image[i][j-1] == color:
                dp(i,j-1)
            while j+1 <len(image[0]) and image[i][j+1] == color:
                dp(i,j+1)


        dp(sr,sc)
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == -1:
                    image[i][j] = newColor
        return image
