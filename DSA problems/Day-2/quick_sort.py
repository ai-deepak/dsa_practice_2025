def quickSort(arr,left,right):
    if left < right:
        mid = (left+right)//2
        pivot=arr[mid]
        index=partition(arr,left,right,pivot)
        quickSort(arr,left,index-1)
        quickSort(arr,index,right)
        
def partition(arr,left,right,pivot):
    while left <= right :
        while arr[left] < pivot:
            left+=1
        while arr[right]>pivot:
            right-=1
        
        if left <= right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return left
    
arr = [34,56,23,12,57,87,23,54,21,76]
quickSort(arr,0,len(arr)-1)
print(arr)