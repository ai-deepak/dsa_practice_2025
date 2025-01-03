def getSecondLargest(arr):
    if len(arr) <= 1:
        return -1
    largest = arr[0]
    secondLargest = arr[1]
    
    for i in range(1,len(arr)):
        if arr[i]>largest:
            secondLargest=largest
            largest=arr[i]
        elif arr[i]!=largest and arr[i]>secondLargest:
            secondLargest=arr[i]
    
    return -1 if largest == secondLargest else secondLargest

arr = [35,12, 1, 10, 34, 1]
print(getSecondLargest(arr))