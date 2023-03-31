"""Ceaser cypher using python standard library"""


from curses.ascii import isupper
import string

def caesar(plain_text, shift_num):
    letters = string.ascii_lowercase
    print(letters)
    mask = letters[shift_num:] + letters[:shift_num]
    print(mask)
    trantab = string.maketrans(letters, mask)   #create a translation table.  
    print(trantab)
    partial_cypher = plain_text.translate(trantab)   #It maps all characters in letters to the corresponding letters in mask and leaves all other characters alone.
    if all(i.isupper() for i in partial_cypher):
        print("Partial Cypher")
    return partial_cypher
text='my name is shahzaib'
print(caesar(text, 4))



#==========================

"""without .translate()"""

# caesar.py
import string

def shift_n(letter, amount):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + amount
    while new_letter > ord("z"):
        new_letter -= 26
    while new_letter < ord("a"):
        new_letter += 26
    return chr(new_letter)

def caesar(message, amount):
    enc_list = [shift_n(letter, amount) for letter in message]
    return "".join(enc_list)



"""NOTE:
ord() does the work of converting a letter to a number, and chr() converts it back to a letter. This is handy as it allows you to do arithmetic on letters, which is what you want for this problem.
"""
