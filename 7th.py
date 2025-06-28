# 7.Count frequency of each element in an list.
def count_frequency(l):
    freq={}
    for i in l:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

print(count_frequency([2,3,3,4,7,5,9]))