from src.aes.aes_encrypt import AESCipher, generate_key
from src.rsa.rsa_encrypt import RSACipher
from src.sha.sha_hash import SHAHasher


def aes_menu():
    print("\n========== AES-256 ==========")

    key = generate_key()
    aes = AESCipher(key)

    message = input("Enter message: ")

    encrypted = aes.encrypt(message)

    print("\nEncrypted Message:")
    print(encrypted)

    decrypted = aes.decrypt(encrypted)

    print("\nDecrypted Message:")
    print(decrypted)


def rsa_menu():
    print("\n========== RSA-2048 ==========")

    rsa = RSACipher()

    rsa.generate_keys()

    message = input("Enter message: ")

    encrypted = rsa.encrypt(message)

    print("\nEncrypted Message:")
    print(encrypted)

    decrypted = rsa.decrypt(encrypted)

    print("\nDecrypted Message:")
    print(decrypted)


def sha_menu():
    print("\n========== SHA Hashing ==========")

    message = input("Enter message: ")

    print("\nMD5:")
    print(SHAHasher.md5(message))

    print("\nSHA1:")
    print(SHAHasher.sha1(message))

    print("\nSHA256:")
    print(SHAHasher.sha256(message))

    print("\nSHA512:")
    print(SHAHasher.sha512(message))


def main():

    while True:

        print("\n")
        print("=" * 50)
        print("Cryptography Algorithms Implementation")
        print("=" * 50)

        print("1. AES Encryption")
        print("2. RSA Encryption")
        print("3. SHA Hashing")
        print("4. Exit")

        choice = input("\nChoose Option: ")

        if choice == "1":
            aes_menu()

        elif choice == "2":
            rsa_menu()

        elif choice == "3":
            sha_menu()

        elif choice == "4":
            print("\nThank you for using the project.")
            break

        else:
            print("\nInvalid Choice!")


if __name__ == "__main__":
    main()