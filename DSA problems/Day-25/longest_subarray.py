#geeksforgeeks
#https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?category%5B%5D=Hash&company%5B%5D=Amazon&page=1&query=category%5B%5DHashcompany%5B%5DAmazonpage1company%5B%5DAmazoncategory%5B%5DHash&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-subarray-with-0-sum


# arr = [-42,12,20,15,31,-4,0,15]

# my solution brute force - time limit exceeded

# maxi=float('-inf')
# num=0
# for i in range(len(arr)):
#     for y in range(i,len(arr)):
#         num = num + arr[y]
#         if num == 0:
#             maxi = max(maxi,y-i+1)
#     num=0
# print(maxi)


#optimal solution
prefix_sum = 0
max_length=0
hashmap={}

for i in range(len(arr)):
    prefix_sum += arr[i]
    if prefix_sum == 0:
        max_length = max(max_length, i + 1)
    if prefix_sum in hashmap:
        idx = hashmap[prefix_sum]
        length = i - idx
        max_length=max(length,max_length)
    else:
        hashmap[prefix_sum]=i

print(max_length)


