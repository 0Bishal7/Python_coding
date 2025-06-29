# 8.Find the second largest number in an array.
def second_largest(l):
    if len(l)<2:
        return None
    largest =second = float("-inf")

    for num in l:
        if num > largest:
            second=largest
            # print(second)
            largest=num
            # second=largest

        elif num > second and num != largest:
            second=num
    return second
print(second_largest([2,5,6.95,3,4,4,6.35]))
        
    
