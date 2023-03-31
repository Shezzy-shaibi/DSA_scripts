
s = "bOitok"
def betterHalvesStringAlike(s):
    vowels = set("aeiouAEIOU")
    diff = 0
    i = 0
    j = len(s) - 1
    while i<j:
        if s[i] in vowels:
            diff +=1
        if s[j] in vowels:
            diff -=1
        i+=1
        j-=1    
    return diff == 0

print(betterHalvesStringAlike(s))

def halvesStringAlike(s):
    first,second = s[:len(s)//2].lower(), s[len(s)//2:].lower()
    print(first,second)
    vowels = {"a", "e", "i", "o", "u"}
    f_count = 0
    s_count=0
    for i in first:
        if i in vowels:
            f_count +=1
    for j in second:
        if j in vowels:
            s_count +=1
    return True if f_count == s_count else False
    
print(halvesStringAlike(s))