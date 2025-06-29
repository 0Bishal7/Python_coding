# 10.Find the missing number in an array of 1 to N.
def find_misiing_number(arr,n):
    expected_sum= n * (n+1) //2
    print(expected_sum)
    acc_sum =sum(arr)
    print(acc_sum)
    return expected_sum-acc_sum

print(find_misiing_number([1,2,3,5],5))