#Largest Element in Array
# https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array

#BRUTE FORCE
def largest(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr[-1]

#OPTIMAL APPROACH
def largest1(arr):
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val

arr = [2,75,48,26,38,99,45,81,21]
print(largest1(arr))