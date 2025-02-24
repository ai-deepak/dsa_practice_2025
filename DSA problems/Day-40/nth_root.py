#geeksforgeeks
#Find nth root of m
#https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-nth-root-of-m


#linear search time complexity O(m log n)
class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        for i in range(1, m + 1):
            ans = i ** n
            if ans == m:
                return i
            elif ans > m:
                return -1


#binary search time complexity  best case - O(log m) and worst case - O(nlogm)

def midpown(mid, n, m):
    ans = 1
    for _ in range(n):  # `_` since index isn't used
        ans *= mid
        if ans > m: 
            return 2  # Return early if exceeding m
    if ans == m: 
        return 1
    return 0

def nthRoot(n, m):
    low = 1
    high = m
    
    while low <= high:
        mid = (low + high) // 2
        res = midpown(mid, n, m)

        if res == 1:
            return mid  # Exact match found
        elif res == 2:
            high = mid - 1  # Reduce search space
        else:
            low = mid + 1  # Increase search space

    return -1  # No integer root found

# Test case
print(nthRoot(2, 9))  # Output: 3
