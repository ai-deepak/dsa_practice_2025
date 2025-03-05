#coding nijas
#https://www.naukri.com/code360/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTabValue=SUBMISSION

#geeksforgeeks
#https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

# i tried to think of a solution but i was not able to come up with a solution
# so i watched strivers explanation and i understood the solution and solved my own binary search solution

#https://www.youtube.com/watch?v=Z0hwjftStI4

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        def allocate(arr,k):
            n=len(arr)
            if k>n:
                return -1
                
            low=max(arr)
            high=sum(arr)
            
            def kcount(arr,mid):
                asum=0
                count=1
                for i in arr:
                    if i+asum <= mid:
                        asum+=i
                    else:
                        asum=i
                        count+=1
                return count
    
            while low<=high:
                mid=(low+high)//2
                k_count = kcount(arr,mid)
                if k_count <= k:
                    high=mid-1
                else:
                    low=mid+1
            
            return low
            
        return allocate(arr,k)
