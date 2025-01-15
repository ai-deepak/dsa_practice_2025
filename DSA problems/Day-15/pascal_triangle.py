# i tried with brute force approach and couldn't come up with optimal solution.

# I have watched the video and understood the solution.
# I have implemented the solution and it is working fine.
# Time complexity is O(n^2) and space complexity is O(1)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        globalList=[]
        res=1
        for num in range(1,numRows+1):
            localList=[]
            for i in range(num):
                if i != 0:
                    res = res * (num-i)
                    res = int(res/i)
                localList.append(res)
            globalList.append(localList)
        return globalList
     