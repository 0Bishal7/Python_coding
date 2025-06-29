# 14.Check if a string contains only digits.
def only_dight(s):
    for char in s :
        if char <"0" or char >"9":
            return False
    return True
print(only_dight("93723737373"))