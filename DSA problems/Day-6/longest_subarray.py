#geeksforgeeks
#https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k

arr = [1, -1, 5, -2, 3]
k = 3
storage=[]
def lenOfLongestSubarr(arr,k):
    for i in range(len(arr)):
        j=i+1
        for y in range(i,len(arr)):
            if arr[i:y]==k:
                storage.append(len(arr[i:y]))


#optimal approach
arr = [1, -1, 5, -2, 3]
k=3
x={} #hashmap
cs=0 #current sum
mx=0 #max length

for i in range(len(arr)):
    cs+=arr[i]
    if cs==k:
        mx=max(mx,i+1)
    rem = cs-k
    if rem in x:
        mx=max(mx,i-x[rem])
    if cs not in x:
        x[cs]=i
print(mx)
