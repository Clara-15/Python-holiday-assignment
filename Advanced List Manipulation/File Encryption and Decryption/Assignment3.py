def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Example
text = "Hello, World!"
shift_value = 3
encrypted_text = encrypt(text, shift_value)
decrypted_text = decrypt(encrypted_text, shift_value)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
