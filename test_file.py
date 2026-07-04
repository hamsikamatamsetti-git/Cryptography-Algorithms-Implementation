from src.aes.aes_encrypt import AESCipher, generate_key

key = generate_key()

aes = AESCipher(key)

aes.encrypt_file(
    "demo/sample.txt",
    "demo/sample.enc"
)

aes.decrypt_file(
    "demo/sample.enc",
    "demo/sample_decrypted.txt"
)

print("File encryption completed.")