#geeksforgeeks
# #Array Leaders
#https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array

#i have done a brute force approach. time complexity is O(N^2) and space is O(N)
# the below code hit the time limit exceeded error.

arr = [16, 17, 4, 3, 5, 2]
newarr=[]
for i in range(len(arr)-1,-1,-1):
    if i==len(arr)-1:
        newarr.append(arr[i])
    j=i+1
    while j < len(arr):
        if arr[i]<arr[j]:
            break
        j+=1
        if j==len(arr):
            newarr.append(arr[i])
newarr = newarr[::-1]
print(newarr)

#optimal approach - solved it using the help of chatgpt explanation.

arr = [16, 17, 4, 3, 5, 2]
newarr = []
max_so_far = float('-inf')

for i in range(len(arr)-1, -1, -1):
    if arr[i] >= max_so_far:
        newarr.append(arr[i])
        max_so_far = arr[i]

newarr.reverse()
print(newarr)
