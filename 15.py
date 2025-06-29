# 15.Implement bubble sort and explain the complexity.
def bubble_Sort(l):
    n=len(l)
    for i in range(n):
        swapped= False

        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped =True
        if not swapped :
            break
    return l

print(bubble_Sort([1,2,7,8,2,4,5]))



