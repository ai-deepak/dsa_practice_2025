#leetcode 
#268. Missing Number


#Brute force
nums = [3,0,1]
for i in range(len(nums)+1):
    if i not in nums:
        print(i)

#Optimal
nums = [3,0,1]
n = len(nums)
defaultSum = (n*(n+1))/2
print(defaultSum - sum(nums))

