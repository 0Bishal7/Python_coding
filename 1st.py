# 1.Reverse a string without using built-in reverse methods.
def reverse_string(s):
    rev_str=""
    for i in s:
        rev_str=i+rev_str
    return rev_str
print(reverse_string("Mrittika"))

# Alternative
def rev_str(s):
    if len(s)==0:
        return s    
    return rev_str(s[1:])+s[0]

    
    
print(rev_str("sayan"))
