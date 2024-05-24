# Minden karaktert bitenként XOR-olja a kulccsal és az egyes karaktereket különböző kulcsértékekkel XOR-olja ráadásul, így előállítva az enkripciót.
# Author Fülöp Bence

def xor_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        current_key = ord(key[i % key_length])
        encrypted_char = (ord(char) + current_key)
        encrypted_text += chr(encrypted_char)
    return encrypted_text

def xor_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        current_key = ord(key[i % key_length])
        decrypted_char = (ord(char) - current_key)
        decrypted_text += chr(decrypted_char)
    return decrypted_text

password = input("Enter your password: ")
key = input("Enter your key: ")

encrypted_password = xor_encrypt(password, key)
print("Encrypted Password:", encrypted_password)

# Ellenőrzés:
decrypted_password = xor_decrypt(encrypted_password, key)
print("Decrypted Password:", decrypted_password)
