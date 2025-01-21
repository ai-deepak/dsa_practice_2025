nums = [2,2]
n = len(nums)
# greater than, so we add +1
minCount = n//3 + 1

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

#optimal (time O(n) and space O(n))