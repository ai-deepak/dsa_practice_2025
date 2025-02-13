#geeksforgeeks
#https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-occurrence
#number of occurence


#linear approach O(n)

class Solution:
    def countFreq(self, arr, target):
        counter=0
        for i in arr:
            if i==target:
                counter+=1
        return counter

#my solution O(logn) or O(k+logn) where k is the number of occurence of target element or O(n) in worst case

arr = [8, 9, 10, 12, 12, 12]
target=12

n=len(arr)
low=0
high=n-1
occ=-1
occ_index=-1
while low<=high:
    
    mid = (low+high)//2

    if arr[mid]==target:
        occ_index=mid
        occ=arr[mid]
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
        

if occ==-1:
    print(0)
    
counter=1
i=occ_index-1
j=occ_index+1

print(i,j,counter)
while i+j!=-2:
    print(i,j,counter)
    if i!=-1:
        if arr[i]==target:
            counter+=1
            if i==0:
                i=-1
            else:
                i-=1
        else:
            i=-1
    if j!=-1:
        if arr[j]==target:
            counter+=1
            if j==(n-1):
                j=-1
            else:
                j+=1
        else:
            j=-1

print(counter)

#chatgpt optimized solution O(logn)
# optimized version using binary search twice to find the first and last occurrences of the target. This reduces the time complexity to O(log n) instead of O(n).

def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # Move left to find first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first

def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1  # Move right to find last occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last

def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0  # Target not found

    last = last_occurrence(arr, target)
    return last - first + 1

# Example usage:
arr = [8, 9, 10, 12, 12, 12]
target = 12
print(count_occurrences(arr, target))  # Output: 3
