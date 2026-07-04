from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os


class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        key = RSA.generate(2048)

        self.private_key = key
        self.public_key = key.publickey()

    def save_keys(self):
        os.makedirs("keys", exist_ok=True)

        with open("keys/private.pem", "wb") as private_file:
            private_file.write(self.private_key.export_key())

        with open("keys/public.pem", "wb") as public_file:
            public_file.write(self.public_key.export_key())

    def load_keys(self):
        with open("keys/private.pem", "rb") as private_file:
            self.private_key = RSA.import_key(private_file.read())

        with open("keys/public.pem", "rb") as public_file:
            self.public_key = RSA.import_key(public_file.read())

    def encrypt(self, message):
        cipher = PKCS1_OAEP.new(self.public_key)

        encrypted = cipher.encrypt(message.encode())

        return base64.b64encode(encrypted).decode()

    def decrypt(self, encrypted_message):
        cipher = PKCS1_OAEP.new(self.private_key)

        encrypted_bytes = base64.b64decode(encrypted_message)

        decrypted = cipher.decrypt(encrypted_bytes)

        return decrypted.decode()


def demo():
    print("=" * 50)
    print("RSA-2048 Encryption Demo")
    print("=" * 50)

    rsa = RSACipher()

    rsa.generate_keys()
    rsa.save_keys()

    message = input("Enter Message: ")

    encrypted = rsa.encrypt(message)

    print("\nEncrypted Message:\n")
    print(encrypted)

    rsa.load_keys()

    decrypted = rsa.decrypt(encrypted)

    print("\nDecrypted Message:\n")
    print(decrypted)


if __name__ == "__main__":
    demo()