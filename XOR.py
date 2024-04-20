# Minden karaktert bitenként XOR-olja a kulccsal, így előállítva az enkripciót.
# Author Fülöp Bence

def xor_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) ^ key)
    return encrypted_text

def xor_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr(ord(char) ^ key)
    return decrypted_text

password = input("Enter your password: ")
key = 256

encrypted_password = xor_encrypt(password, key)
print("Encrypted Password:", encrypted_password)

# Ellenőrzés:
#decrypted_password = xor_decrypt(encrypted_password, key)
#print("Decrypted Password:", decrypted_password)
