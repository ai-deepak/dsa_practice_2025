#coding ninjas
#Painter's Partition Problem
#https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM


#same problem in geeksforgeeks
#https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1

#solved on my own
def findLargestMinDistance(boards:list, k:int):

    def painter(arr,k):
        n=len(arr)
        low=max(arr)
        high=sum(arr)
        
        def traverse(arr,mid):
            asum, count = 0,1
            for i in arr:
                if i+asum > mid:
                    count+=1
                    asum=i
                else:
                    asum+=i
            return count
                
        while low<=high:
            mid = (low+high)//2
            k_count = traverse(arr,mid)
            if k_count <= k:
                high=mid-1
            else:
                low=mid+1
        
        return low

    return painter(boards,k)