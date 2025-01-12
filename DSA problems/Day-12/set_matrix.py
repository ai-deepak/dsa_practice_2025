#leetcode
# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/
#my solution - O(N^2) for time and space

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        if row==1 and col==1:
            return;
        newset=set()
        def addPairs(i,j,row,col):
            #keep j constant
            for x in range(col):
                newset.add((i,x))
            #keep i constant
            for y in range(row):
                newset.add((y,j))

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    addPairs(i,j,row,col)
        for i in newset:
            matrix[i[0]][i[1]]=0

#chatgpt-updated solution - O(N^2) for time and O(1) for space

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set matrix cells to zero based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Update the first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Update the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
