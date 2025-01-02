def selection_sort(arr):
    if len(arr)>1:
        for i in range(len(arr)):
            for y in range(i+1,len(arr)):
                if arr[y]<arr[i]:
                    arr[i],arr[y]=arr[y],arr[i]
arr = [1,4,3,2,6,8]
selection_sort(arr)
print(arr)