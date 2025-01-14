# tried and couldn't come up with solution. Hence watched the video.
#brute force approach is to rotate the array using another empty array.
# Time complexity is O(n^2) and space complexity is O(n^2)

#Optimal approach
# Time complexity is O(n^2) and space complexity is O(1)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()