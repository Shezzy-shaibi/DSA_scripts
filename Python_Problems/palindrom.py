"""A Word which should be same either we right it in reverse order as MADAM"""



def palindrom(w):
    str_word = str(w)
    if str_word == str_word[::-1]:
        return True
    else:
        return False
    
 
print(palindrom("mam"))


def isPalindrom(word):
    return True if word == word[::-1] else False

print(isPalindrom("madam"))