#geeksforgeeks
#Sorted Array Search
#https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win


#my solution is recursive binary search with slicing
#hence my time complexity is O(n) and space is O(n)

arr = [1, 2, 3, 4, 6]
k = 6
def search(arr,k):
    if len(arr)<1:
        return False
    mid = len(arr)//2
    if arr[mid]==k:
        return True
    elif arr[mid]<k:
        return search(arr[mid+1:],k)
    else:
        return search(arr[:mid],k)

print(search(arr,k))


# to make it better, we can do same recursion without slicing.
# which will bring it time and space complexity to O(log n)
# below is the solution

arr = [1, 2, 3, 4, 6]
k = 6

def search(arr, k, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] == k:
        return True
    elif arr[mid] < k:
        return search(arr, k, mid + 1, high)
    else:
        return search(arr, k, low, mid - 1)

print(search(arr, k, 0, len(arr) - 1))


#even more optimal solution is to avoid recursion and do iterative binary search.
# which will bring it time complexity to O(log n) and space to O(1)
# below is the solution
arr = [1, 2, 3, 4, 6]
k = 6

def search(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return True  # Element found
        elif arr[mid] < k:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return False  # Element not found

print(search(arr, k))
