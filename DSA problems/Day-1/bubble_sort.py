def bubble_sort(arr):
    for i in range(len(arr)):
        for y in range(len(arr)-i-1):
            if arr[y]>arr[y+1]:
                arr[y],arr[y+1]=arr[y+1],arr[y]

arr = [1,4,3,2,6,8]
bubble_sort(arr)
print(arr)