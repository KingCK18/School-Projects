"""
Created on 10/21/23
@author: christiankirby
"""

lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = lower_alpha.upper()

shift = 3
shifted_lower = lower_alpha[3:] + lower_alpha[:3]
shifted_upper = upper_alpha[3:] + upper_alpha[:3]

def encrypt(text):
    """
    functions that encrypts text into Caesar Cipher based on the integer
    used to shift the text
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                index = lower_alpha.index(char)
                encrypted_char = shifted_lower[index]
            elif char.isupper():
                index = upper_alpha.index(char)
                encrypted_char = shifted_upper[index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def findShift(words):
    """
    function that returns the integer that was used to shift into Caesar Cipher
    """
    import os.path
    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    cleanwords = set([w.strip() for w in f.read().split()])

    best_shift = 0
    max_match = 0

    for s in range(26):
        setShift(s)
        decrypted_text = encrypt(words)
        max_word_count = len(set(decrypted_text.split()).intersection(cleanwords))

        if max_word_count > max_match:
            max_match = max_word_count
            best_shift = 26 - int(s)
    return best_shift

def setShift(new_shift):
    """
    function that assigns a new shift to the helper function shift
    """
    global shifted_lower
    shifted_lower = lower_alpha[new_shift:] + lower_alpha[:new_shift]
    global shifted_upper
    shifted_upper = upper_alpha[new_shift:] + upper_alpha[:new_shift]
    global shift
    shift = new_shift

if __name__ == '__main__':
    print('Hey!')
    words = 'Zkdw grhv wkh ira vbd'
    print(findShift(words))
