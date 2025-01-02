def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1

arr = [1,4,3,2,6,8]
insertion_sort(arr)
print(arr)