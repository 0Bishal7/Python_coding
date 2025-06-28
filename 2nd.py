def is_palindrome(n):
    original=n           
    reverse_n =0
    while n >0:
        dight= n % 10     
        reverse_n= reverse_n * 10 +dight
        n= n//10
    return original == reverse_n

print(is_palindrome(121))

