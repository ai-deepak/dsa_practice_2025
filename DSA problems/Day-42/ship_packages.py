#leetcode
#1011. Capacity To Ship Packages Within D Days
#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/


#solved it myself using binary search

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def ship(weights,days):
            low=max(weights)
            high=sum(weights)
            
            def reqDays(weights,mid):
                days,load=1,0
                for i in weights:
                    if load+i>mid:
                        days+=1
                        load=i
                    else:
                        load+=i
                return days
                
            while low<high:
                mid=(low+high)//2
                days_it_took = reqDays(weights,mid)
                print(low,mid,high,days_it_took)
                
                if days_it_took<=days:
                    high=mid
                else:
                    low=mid+1
            
            return low

        return ship(weights,days)