#interviewbit
#https://www.interviewbit.com/problems/subarray-with-given-xor/

#watched striver video and solved on my own
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xr = 0
        count=0
        hashmap={0:1}
        for i in range(len(A)):
            xr = xr ^ A[i]
            searchVal = xr ^ B
            if searchVal in hashmap:
                count+=hashmap[searchVal]
            if xr in hashmap:
                hashmap[xr]+=1
            else:
                hashmap[xr]=1
                
        return count
