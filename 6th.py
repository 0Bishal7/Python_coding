# 6.Remove duplicates from a list/array.
def remove_duplicates(l):
    result=[]
    seen =set()
    for i in l:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result
print(remove_duplicates([2,5,3,9,6,2,39,9,3]))