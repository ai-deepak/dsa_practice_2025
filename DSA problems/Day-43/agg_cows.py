#spoj
#aggressive cows
#https://www.spoj.com/problems/AGGRCOW/

#geeksforgeeks
#https://www.geeksforgeeks.org/problems/aggressive-cows/0


#for question understanding watch striver video
#https://www.youtube.com/watch?v=R_Mfw4ew-Vo

#after watching striver video, implementing on my own binary search

arr = [0,3,4,7,9,10]
cows=4

arr.sort() #required only if arr is not sorted.

def isPossible(arr,cows,minD):
    i=1
    j=0
    cow_cnt=1
    while i < len(arr):
        print(f"current cow_count={cow_cnt}")
        print(f"i={i}, j={j}, hence {arr[i]}-{arr[j]}")
        length = arr[i]-arr[j]
        print(f"length is {length}")

        if minD<=length:
            print(f"min required distance is {minD} which is lessar than equal to {length}")
            cow_cnt+=1
            print(f"incremented cow count to {cow_cnt}")
            j=i
            print(f"now j = {j}")
            if cow_cnt==cows:
                return True
        i+=1
        print(f"end of iteration, incremented i = {i}")
        
    return False

def aggcows(arr,cows):
    
    low = 1
    high = max(arr)-min(arr)
    
    while low <= high:
        mid = (low+high)//2
        if isPossible(arr,cows,mid):
            low=mid+1
        else:
            high=mid-1
    
    return high

print(aggcows(arr,cows))