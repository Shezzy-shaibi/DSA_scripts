
s1 = "thequickbrownfoxjumpsoverthelazydog"
def IsPangram(sentence):
    if len(set(sentence)) == 26:
        return True
    else:
        return False
print(IsPangram(s1))