# 5.Implement a function to find the largest element in an array.
def largest(arr):
    if len(arr)==0:
        return None 
    largest=arr[0]
    for i in arr:
        if i > largest:
            largest=i
    return largest

print(largest([1,7,8,9,2,3]))