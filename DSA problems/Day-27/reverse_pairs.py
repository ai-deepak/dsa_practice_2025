#leetcode
# reverse pairs
# https://leetcode.com/problems/reverse-pairs/description/
# first hard problem

# brute force - tried to solve, but time limit exceeded

nums = [2,4,3,5,1]
n = len(nums)
counter = 0
for i in range(n):
    for j in range(i+1,n):
        print(f"(i,j)=({i},{j})")
        if nums[i] > (2*nums[j]):
            counter+=1
print(counter)

# optimal solution
