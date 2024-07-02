"""
Created on 10/19/23
@author: christiankirby
"""
def no_vowels(word):
    """
    function checks if the word has no vowels
    """
    for char in word:
        if char in "aeiouyAEIOUY":
            return False
    return True

def not_a_vowel(word):
    """
    function that checks if the character in the word is not a vowel
    """
    for char in word:
        if char in "aeiouyAEIOUY":
            return word[word.index(char):] + "-" + word[0:word.index(char)] + "ay"
    return " "
def const_with_Y(word):
    """
    if the word starts with y than based off of certain criteria, it will
    return the correct pig latin version
    """
    for char in word:
        if char in "aeiou":
            return word[word.index(char):] + "-" + word[0:word.index(char)] + "ay"
    return " "

def const_with_Qu(word):
    """
    if the word starts with qu than based off of certain criteria, it will
    return the correct pig latin version
    """
    if word.startswith("qu") or word.startswith("QU"):
        return word[2:] + "-quay"
    for char in word[2:]:
        if char in "aeiou":
            return word[word.index(char):] + "-qu" + word[2:word.index(char)] + "ay"
    return ""
def encrypt(string):
    """
    function that takes a word and encrypts it into Pig Latin based on the
    category the word falls into
    """
    string = string.split()
    encrypted_words = []
    for word in string:
        if word[0] in "aeiouAEIOU":
            encrypted_words += [word + "-way"]
        elif (word[0:2] in 'QU' or word[0:2] in 'qu' and word[2] not in
              'aeiouyAEIOUY'):
            return word[3:] + '-' + word[0:3] + 'ay'
        elif word[0:2] in 'Qu'or word[0:2] in 'qu':
            encrypted_words += const_with_Qu(word)
        elif no_vowels(word):
            encrypted_words += [word + "-way"]
        elif word[0] in ['y','Y']:
            encrypted_words += const_with_Y(word)
        else:
            encrypted_words += not_a_vowel(word)
    return "".join(encrypted_words)

def const_dec(word):
    """
    function that helps the function decrypt locate the proper consonants
    """
    for char in word[2:]:
        if "-" in word[2:]:
            return word[word.index(char):-2] + word[:word.index(char)]
    return " "

def decrypt(string):
    """
    function that decrypts the pig latin-ized word
    """
    if string[-4:-1] == "-way":
        decrypted_words = string.split("-")[0]
    else:
        decrypted = string.split("-")
        decrypted_words = decrypted[1][:-2] + decrypted[0]
    return decrypted_words





if __name__ == '__main__':

    print(encrypt("yesterday"))
    print(decrypt("ello-hay"))
    print(encrypt("quiz"))
    print(encrypt("qupo"))
    print(encrypt('ZZZZZZ'))









