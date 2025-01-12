#leetcode
# 2149. Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

# i coded the below solution myself. Got time limit exceeded error.
# Time Complexity:
# Worst-case 
# 𝑂(𝑛^2)
# O(n^2) because of the nested swapping loop for each i.
# Space Complexity:
# 𝑂(1)
# O(1) since the rearrangement is done in-place.


nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
#output = [28,-41,22,-8,46,-37,35,-9,18,-6,19,-26,15,-37,14,-10,31,-9]

i,j = 0,1

def isNegative(val):
    return val < 0
def isPositive(val):
    return val >=0

while i < len(nums):
    if i % 2 ==0:
        print("===============Even Index================")
        if isNegative(nums[i]):
            print("~~~~~~~the problem starts~~~~~~~")
            print(f"{nums[i]} is not Positive")
            if isPositive(nums[j]):
                print(f"j={nums[j]} is Positive, Do swapping")
                print(f"These 2 numbers swap each other {nums[i]} and {nums[j]}")
                while i < j:
                    if i==(j-1):
                        nums[i],nums[j]=nums[j],nums[i]
                        break
                    else:
                        nums[j],nums[j-1]=nums[j-1],nums[j]
                        j-=1
                print(f"now array looks like = {nums}")
            else:
                print(f"j={nums[j]} is not Positive, Hence increment J")
                j+=1
                continue
        else:
            print(f"{nums[i]} is Positive, hence no prob")
    elif i % 2 ==1:
        print("================Odd Index================")
        if isPositive(nums[i]):
            print("~~~~~~~the problem starts~~~~~~~")
            print(f"{nums[i]} is not Negative")
            if isNegative(nums[j]):
                print(f"j={nums[j]} is Negative, Do swapping")
                print(f"These 2 numbers swap each other {nums[i]} and {nums[j]}")
                while i < j:
                    if i==(j-1):
                        nums[i],nums[j]=nums[j],nums[i]
                        break
                    else:
                        nums[j],nums[j-1]=nums[j-1],nums[j]
                        j-=1
                print(f"now array looks like = {nums}")
            else:
                print(f"j={nums[j]} is not Negative, Hence increment J")
                j+=1
                continue
        else:
            print(f"{nums[i]} is Negative, hence no prob")
    i+=1
    j=i+1
print(nums)


#chatgpt proposed me a solution, which i initially thought which increases space complexity
# the code is storing positive and negative in separate array.
# using for loop, merging the array.
# time complexity is O(2N) for both time and space

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        # Merge them in alternating order
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])

        return result

#after watching striver video, a slightly better solution
# time complexity is O(N) for both time and space

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newArr=[0]*len(nums)
        pos=0
        neg=1
        for i in range(len(nums)):
            if nums[i]>=0:
                newArr[pos]=nums[i]
                pos+=2
            elif nums[i]<0:
                newArr[neg]=nums[i]
                neg+=2
        return newArr











