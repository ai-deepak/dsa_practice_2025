#geeksforgeeks
#Maximum Score from Subarray Minimums
#https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays

#I solved this in optimal solution at first. I found a pattern in this problem, which i feel proud of myself.
# how did i find pattern?
# initially i crafted this code based on example

arr = [5, 4, 3, 1, 6] 

for i in range(len(arr)):
    for y in range(i+2,len(arr)+1):
        print(arr[i:y])

# This is the output i got
# [5, 4]
# [5, 4, 3]
# [5, 4, 3, 1]
# [5, 4, 3, 1, 6]
# [4, 3]
# [4, 3, 1]
# [4, 3, 1, 6]
# [3, 1]
# [3, 1, 6]
# [1, 6]

# we have to find smallest and second smallest in all of the array 
# and we need to return the largest sum of it

# if i continued with the above code, the time complexity would have been O(N^3).
# but when i looked at the output. I saw a pattern, let me arrange the output in different way.

# This is the output
# array with 2 elements
# [5, 4]
# [4, 3]
# [3, 1]
# [1, 6]
# array with greater than 2 elements
# [5, 4, 3] ==> [4,3]
# [5, 4, 3, 1] ==> [3,1]
# [5, 4, 3, 1, 6] ==> [3,1]
# [4, 3, 1] ==> [3,1]
# [4, 3, 1, 6] ==> [3,1]
# [3, 1, 6] ==> [3,1]

#when you look at the array with greater than 2 elements and their smallest and second smallest. 
# it is be always be present in array with 2 elements.
# we do not need to check array with greater than 2 elements. This eliminates multiple for loop.
# we need only single for loop. check 2 numbers, sum it, find the overall max.

#below is the code optimized O(N) time and O(1) space
# # Your code goes here
asum=0
for i in range(len(arr)-1):
    asum = max((arr[i]+arr[i+1]),asum)
print(asum)