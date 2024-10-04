"""
Caesar cipher functions
"""

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            if letter == "X":
                ciphertext += "A"
            elif letter == "x":
                ciphertext += "a"
            elif letter == "Y":
                ciphertext += "B"
            elif letter == "y":
                ciphertext += "b"
            elif letter == "Z":
                ciphertext += "C"
            elif letter == "z":
                ciphertext += "c"
            else:
                ciphertext += chr(ord(letter)+shift)
        else:
            ciphertext += letter

    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            if letter == "A":
                plaintext += "X"
            elif letter == "a":
                plaintext += "x"
            elif letter == "B":
                plaintext += "Y"
            elif letter == "b":
                plaintext += "y"
            elif letter == "C":
                plaintext += "Z"
            elif letter == "c":
                plaintext += "z"
            else:
                plaintext += chr(ord(letter) - shift)
        else:
            plaintext += letter
    return plaintext