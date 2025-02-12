#coding ninja
# https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=PROBLEM

#optimal solution *binary search*
def getFloorAndCeil(a, n, x):
    # Write your code here.
    low=0
    high=n-1
    floor=-1
    ceiling=-1
    while low<=high:
        mid=(low+high)//2

        if a[mid]==x:
            floor=ceiling=a[mid]
            break
        elif a[mid]<=x:
            floor=a[mid]
            low=mid+1
        else:
            ceiling=a[mid]
            high=mid-1
    return [floor,ceiling]