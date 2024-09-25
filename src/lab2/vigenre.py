"""
Vigenere cipher functions
"""
alpha = [chr(i) for i in range (ord("A"),ord("Z")+1)] + [chr(i) for i in range (ord("A"),ord("Z")+1)] + [chr(i) for i in range (ord("a"), ord("z")+1)] + [chr(i) for i in range (ord("a"), ord("z")+1)]

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    if len(keyword)<len(plaintext):
        keyword *= len(plaintext)

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            ciphertext += alpha[ alpha.index(plaintext[i]) + (alpha.index(keyword[i]))%52 ]
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    if len(keyword) < len(ciphertext):
        keyword *= len(ciphertext)

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            plaintext += alpha[ alpha.index(ciphertext[i]) - (alpha.index(keyword[i])) % 52 +26]
        else:
            plaintext += ciphertext[i]
    return plaintext