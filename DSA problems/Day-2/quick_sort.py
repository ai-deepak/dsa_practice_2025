#Setting Pivot as last Element

def quick_sort(arr,left,right):
    if left < right:
        partition_pos = partition(arr,left,right)
        quick_sort(arr,left,partition_pos-1)
        quick_sort(arr,partition_pos+1,right)

def partition(arr,left,right):
    i=0
    j=right-1
    pivot=arr[right]

    while i < j:
        while arr[i] < arr[right]:
            i+=1
        while arr[j] > arr[right]:
            j-=1
    if arr[i]>arr[right]:
        arr[i],arr[right]=arr[right],arr[i]
    return i

arr = [1,4,3,2,6,8]
quick_sort(arr,0,len(arr)-1)
print(arr)