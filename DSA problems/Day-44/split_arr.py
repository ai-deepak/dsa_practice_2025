#leetcode
#410. Split Array Largest Sum
#https://leetcode.com/problems/split-array-largest-sum/description/

# i solved it myself using binary approach. but took some tiny help from chatgpt.
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splitarr(nums,k):
            low=max(nums)
            high=sum(nums)
            
            def traverse(nums,mid):
                asum, count = 0,1
                for i in nums:
                    if i+asum<=mid:
                        asum+=i
                    else:
                        asum=i
                        count+=1
                return count
                
                
            while low<=high:
                
                mid=(low+high)//2
                
                kcount = traverse(nums,mid)
                if kcount > k:
                    low=mid+1
                else:
                    high=mid-1
            
            return low
            
        return splitarr(nums,k)
                
