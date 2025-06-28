# 4.Check if a string is an anagram of another.?
def anagram(s1,s2):
    s1=s1.replace("","").lower()
    s2=s2.replace("","").lower()
    if len(s1)!=len(s2):
        return False
    char_count={}
    for i in s1:
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i]=1
    for i in s2:
        if i not in char_count:
            return False
        char_count[i]-=1
        if char_count[i]<0:
            return False
    return True
print(anagram("Integral","Triangle"))