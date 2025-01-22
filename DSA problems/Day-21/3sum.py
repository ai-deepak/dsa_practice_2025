#leetcode
# 15. 3Sum
# https://leetcode.com/problems/3sum/

# tried brute force myself, didn't work
# watched striver video

# solution 1
nums = [-1,0,1,2,-1,-4]
n = len(nums)
i=0
nums.sort()
res = set()
print(nums)
for i in range(n):
    j=i+1
    k=n-1
    while j<k:
        print(f"currVal={nums[i]},jVal={nums[j]},kVal={nums[k]}")
        alsum = nums[i]+nums[j]+nums[k]
        print(f"sum={alsum}")
        if alsum == 0:
            res.add((nums[i],nums[j],nums[k]))
            j+=1
            k-=1
        elif alsum < 0:
            print("incrementing J")
            j+=1
        elif alsum > 0:
            print("Decrementing K")
            k-=1

print(list(res))

# solution2: 
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0
        
        for x in nums:
            if x < 0:
                neg[x] += 1
            elif x > 0:
                pos[x] += 1
            else:
                zeros += 1
        
        r = []
        
        if zeros:
            for n in neg:
                if -n in pos:
                    r.append((0, n, -n))
        
            if zeros > 2:
                r.append((0,0,0))

        for set_a, set_b in ((neg, pos), (pos, neg)):
            set_a_items = list(set_a.items())
            for i, (x, q) in enumerate(set_a_items):
                for x2, q2 in set_a_items[i:]:
                    if x != x2 or (x == x2 and q > 1):
                        if -x-x2 in set_b:
                            r.append((x, x2, -x-x2))

        return r
        