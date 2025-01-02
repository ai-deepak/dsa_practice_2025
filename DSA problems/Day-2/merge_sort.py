def merge_sort(arr):
    if len(arr) <= 1:  # Guard clause for base case
        return
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]
    merge_sort(left_arr)
    merge_sort(right_arr)

    #merging
    i = 0 #left arr index
    j = 0 #right arr index
    k = 0 #main arr index

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i]<right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k]=right_arr[j]
            j+=1
        k+=1
    while i < len(left_arr):
        arr[k]=left_arr[i]
        i+=1
        k+=1
    while j < len(right_arr):
        arr[k]=right_arr[j]
        j+=1
        k+=1

arr = [1,4,3,2,6,8]
merge_sort(arr)
print(arr)