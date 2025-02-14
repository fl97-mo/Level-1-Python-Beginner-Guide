import random

def caesar_encrypt(text):
    shift = random.randint(1, 25)  
    encrypted_text = ''.join(chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else
                             chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper() else c
                             for c in text)
    return encrypted_text, shift

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ''.join(chr((ord(c) - 97 - shift) % 26 + 97) if c.islower() else
                             chr((ord(c) - 65 - shift) % 26 + 65) if c.isupper() else c
                             for c in encrypted_text)
    return decrypted_text


original_text = "HelloWorld"
encrypted_text, shift = caesar_encrypt(original_text)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print(f"Original: {original_text}")
print(f"Encrypted: {encrypted_text} (Shift: {shift})")
print(f"Decrypted: {decrypted_text}")
