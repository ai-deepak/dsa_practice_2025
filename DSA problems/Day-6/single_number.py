#leetcode
#136. Single Number


#brute force approach 

nums = [2,2,1,3,3,4,4]
storage={}
def singleNumber(nums):
    for i in nums:
        if i in storage:
            storage[i]+=1
        else:
            storage[i]=1
    for i,j in storage.items():
        if j == 1:
            return i

print(singleNumber(nums))
print(storage)

#Overall Time  Complexity:O(n).
#Overall Space Complexity:O(n).


#optimal solution using XOR operation (bit manipulation concept)
result = 0
for num in nums:
    result ^= num
print(result)