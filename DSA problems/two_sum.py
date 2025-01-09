#i tried myself a two pointer approach. but failed in test cases. so gave up. and watched striver video.
#brute force solution is typical search one by one for match which is O(N^2) time complexity.
#He also suggested for hashing, which i coded below.
#here the complexity is O(N) for both time and space.
nums = [3,3]
target = 6
numDict={}
for i in range(len(nums)):
    rem = target - nums[i]
    print(f"rem={rem}")
    if rem in numDict:
        print([numDict.get(rem),i])
        break
    numDict[nums[i]]=i
    print(numDict)

#if interviewer asks to avoid hashmaps, then use 2 pointer approach but you can solve
# by giving the output as Yes or No, instead of returning the index.
# if index to be returned, then we need to somehow store the index in another datastructure in array or tuple.