# 12.Implement linear and binary search.
def linear_binary(arr,target):           # Both works for sorted list or unsorted list 
    for i in range(len(arr)):
        if arr[i]== target:
            return i
    return -1

print(linear_binary([1,5,7,8,9,10,23],10))


def binary_search(arr,target):
    low=0
    high= len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high= mid-1
    return -1
print(binary_search([1, 3, 5, 7, 9, 11] ,7))
