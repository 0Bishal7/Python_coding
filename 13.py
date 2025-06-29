# 13.Count vowels and consonants in a string.
def vowels_consonet(s):
    s=s.lower()
    v="aeiou"
    v_count=0
    c_count=0
    for i in s:
        if i.isalpha():# Ignore numbers, spaces, symbols
            if i in v :
                v_count+=1
            else:
                c_count +=1
    return f"vowel: {v_count} , consonet: {c_count}"

print(vowels_consonet("sayan"))
