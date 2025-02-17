#leetcode
#33. Search in Rotated Sorted Array
#https://leetcode.com/problems/search-in-rotated-sorted-array/description/


# after watching striver video

nums = [4,5,6,7,0,1,2]
target = 0

def sorted_rotated_array(nums):
    n=len(nums)
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target: return mid
        if nums[low]<=nums[mid]:
            if target >=nums[low] and target <=nums[mid]:
                high=mid-1
            else:
                low=mid+1	
        else: 
            #right array is sorted
            if target >= nums[mid] and target <=nums[high]:
                low=mid+1
            else:
                high=mid-1

    return -1

print(sorted_rotated_array(nums))
#explanation

# Find the mid
# We need to check which array is sorted- this will help us eliminate the half at each iteration by helping us identify where the target is.
# We need to iterate till we reach low<=high
# If left array is sorted, check low and mid
# If target is between or equal to low and mid, then eliminate right half by setting high to mid-1
# if not, set low to mid+1
# If right array is sorted, check mid and high
# If target is between or equal to mid and high, then eliminate left half by setting low to mid+1
# If not, set high to mid-1
# Always check if mid==target initially, return mid
# If target is not present, loop will end and you return -1, at last
