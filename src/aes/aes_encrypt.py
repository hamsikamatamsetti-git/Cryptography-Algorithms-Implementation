from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


class AESCipher:
    """
    AES-256 Encryption and Decryption
    """

    def __init__(self, key=None):
        if key is None:
            self.key = get_random_bytes(32)
        else:
            self.key = key

    def encrypt(self, plaintext):
        """
        Encrypt plaintext using AES-256-CBC
        """
        cipher = AES.new(self.key, AES.MODE_CBC)

        encrypted = cipher.encrypt(
            pad(plaintext.encode("utf-8"), AES.block_size)
        )

        encrypted_data = base64.b64encode(
            cipher.iv + encrypted
        ).decode("utf-8")

        return encrypted_data

    def decrypt(self, encrypted_text):
        """
        Decrypt AES ciphertext
        """
        encrypted_data = base64.b64decode(encrypted_text)

        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        decrypted = unpad(
            cipher.decrypt(ciphertext),
            AES.block_size
        )

        return decrypted.decode("utf-8")

    def encrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as file:
            data = file.read()

        cipher = AES.new(self.key, AES.MODE_CBC)

        encrypted = cipher.encrypt(
            pad(data, AES.block_size)
        )

        with open(output_file, "wb") as file:
            file.write(cipher.iv + encrypted)

    def decrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as file:
            data = file.read()

        iv = data[:16]
        ciphertext = data[16:]

        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        decrypted = unpad(
            cipher.decrypt(ciphertext),
            AES.block_size
        )

        with open(output_file, "wb") as file:
            file.write(decrypted)


def generate_key():
    """
    Generate AES-256 key
    """
    return get_random_bytes(32)


def save_key(key, filename="keys/aes_key.bin"):
    with open(filename, "wb") as file:
        file.write(key)


def load_key(filename="keys/aes_key.bin"):
    with open(filename, "rb") as file:
        return file.read()


def demo():
    print("=" * 50)
    print("AES-256 Encryption Demo")
    print("=" * 50)

    key = generate_key()

    save_key(key)

    aes = AESCipher(key)

    message = input("Enter Message : ")

    encrypted = aes.encrypt(message)

    print("\nEncrypted Message:\n")
    print(encrypted)

    decrypted = aes.decrypt(encrypted)

    print("\nDecrypted Message:\n")
    print(decrypted)


if __name__ == "__main__":
    demo()