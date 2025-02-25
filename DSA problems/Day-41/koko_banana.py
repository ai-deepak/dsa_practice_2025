#leetcode
# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/

# solved using binary search O(NlogM) where N is the number of piles and M is the maximum number of bananas in a pile
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def sum_ops(piles,mid):
            pilesum = 0
            for i in piles:
                pilesum=pilesum + math.ceil(i/mid)
            return pilesum
            
        def koko(piles,h):
            low=1
            high=max(piles)
            ans=0
            while low<=high:
                mid=(low+high)//2
                res = sum_ops(piles,mid)
                if res <= h:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
            
        return koko(piles,h)