# nums = [2,2]
# n = len(nums)
# # greater than, so we add +1
# minCount = n//3 + 1

#brute force (time O(n^2) and space O(n))
# check=[]
# res=[]
# def brute(nums,n,minCount):
#     for i in range(n):
#         currVal=nums[i]
#         counter=0
#         if currVal not in check:
#             for y in range(i,n):
#                 if currVal==nums[y]:
#                     counter+=1
#             if counter >= minCount:
#                 res.append(currVal)
#             check.append(currVal)
#     return res

# print(brute(nums,n,minCount))


#better (time O(n) and space O(n))
# sDict={}
# res=[]
# def better(nums,n,minCount):
#     for i in range(n):
#         currVal=nums[i]
#         if currVal in sDict:
#             sDict[currVal]+=1
#         else:
#             sDict[currVal]=1
#         if sDict.get(currVal)>=minCount and currVal not in res:
#             res.append(currVal)
#         if len(res)==2: break
            
#     return res

# print(better(nums,n,minCount))

#optimal (time O(n) and space O(1)) Moore's Voting Algorithm

def optimal(nums,n,minCount):
    counter1=0
    counter2=0
    ele1=0
    ele2=0
    res=[]
    for i in range(n):
        if counter1==0 and nums[i]!=ele2:
            counter1=1
            ele1=nums[i]
        elif counter2==0 and nums[i]!=ele1:
            counter2=1
            ele2=nums[i]
        elif ele1==nums[i]:
            counter1+=1
        elif ele2==nums[i]:
            counter2+=1
        else:
            counter1-=1
            counter2-=1
    counter1=0
    counter2=0
    for i in range(n):
        if nums[i]==ele1:
            counter1+=1
        elif nums[i]==ele2:
            counter2+=1
    if counter1 >= minCount:
        res.append(ele1)
    if counter2 >= minCount:
        res.append(ele2)
    return res

# print(optimal(nums,n,minCount))