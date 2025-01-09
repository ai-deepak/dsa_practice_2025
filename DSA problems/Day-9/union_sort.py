#geeks for geeks
#Union of 2 Sorted with Duplicates
#https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays

#my solution got time limit exceed error. but solved 10 testcase, it is taking more than 2 sec.
# my solution uses 3 while loop, i guess O(2N) time complexity.
## my approach O(N^2) in the worst case due to the repeated use of the `not in` check within the loops.
### Complexity Analysis:
# 1. **Time Complexity**:
#    - The first while loop processes all elements in `a` and `b`, iterating a total of \( O(m + n) \), where \( m = \text{len}(a) \) and \( n = \text{len}(b) \).
#    - The second and third while loops run \( O(m) \) and \( O(n) \) in total.
#    - Checking for duplicates in `c` using `not in` has \( O(k) \), where \( k \) is the current length of `c`. This could result in \( O((m+n)^2) \) in the worst case.

# 2. **Space Complexity**:
#    - The result array `c` has \( O(m + n) \) space in the worst case.


a = [-8, -3, -3, -2, 0, 1, 2, 2, 6]
b = [-9, -9, 0]
i,j=0,0
c = []
while i < len(a) and j < len(b):
    print(f"a[i]={a[i]} and b[j]={b[j]}")
    if a[i]==b[j]:
        print("equal")
        if a[i] not in c:
            c.append(a[i])
            j+=1
        i+=1
    elif a[i]<b[j]:
        print("lesser")
        if a[i] not in c:
            c.append(a[i])
        i+=1
    else:
        print("greater")
        if b[j] not in c:
            c.append(b[j])
        j+=1
    print(c)
while i < len(a):
    if a[i] not in c:
        c.append(a[i])
    i+=1
while j < len(b):
    if b[j] not in c:
        c.append(b[j])
    j+=1
print(c)

### chatgpt solution with O(N) time and O(N) space
### Optimized Version: \( O(m + n) \)
# If you use a `set` to track duplicates, the membership check becomes \( O(1) \) (amortized). This reduces the overall complexity to \( O(m + n) \), since each element is processed exactly once, and membership checks are constant time.

# By replacing:
# ```python
# if a[i] not in c:
# ```
# with:
# ```python
# if a[i] not in seen:
# ```
# (where `seen` is a set), you achieve linear time complexity.

a = [-8, -3, -3, -2, 0, 1, 2, 2, 6]
b = [-9, -9, 0]
i, j = 0, 0
c = []
seen = set()

while i < len(a) and j < len(b):
    if a[i] == b[j]:
        if a[i] not in seen:
            c.append(a[i])
            seen.add(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        if a[i] not in seen:
            c.append(a[i])
            seen.add(a[i])
        i += 1
    else:
        if b[j] not in seen:
            c.append(b[j])
            seen.add(b[j])
        j += 1

while i < len(a):
    if a[i] not in seen:
        c.append(a[i])
        seen.add(a[i])
    i += 1

while j < len(b):
    if b[j] not in seen:
        c.append(b[j])
        seen.add(b[j])
    j += 1

print(c)


#striver solution, same but instead of set, they handled in if condition.

def find_union(arr1, arr2):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)



