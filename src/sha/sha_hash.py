import hashlib


class SHAHasher:
    """
    SHA Hashing Algorithms
    """

    @staticmethod
    def sha256(text):
        return hashlib.sha256(text.encode()).hexdigest()

    @staticmethod
    def sha512(text):
        return hashlib.sha512(text.encode()).hexdigest()

    @staticmethod
    def md5(text):
        return hashlib.md5(text.encode()).hexdigest()

    @staticmethod
    def sha1(text):
        return hashlib.sha1(text.encode()).hexdigest()


def demo():
    print("=" * 50)
    print("SHA Hash Generator")
    print("=" * 50)

    message = input("Enter Message: ")

    print("\nMD5 Hash:")
    print(SHAHasher.md5(message))

    print("\nSHA-1 Hash:")
    print(SHAHasher.sha1(message))

    print("\nSHA-256 Hash:")
    print(SHAHasher.sha256(message))

    print("\nSHA-512 Hash:")
    print(SHAHasher.sha512(message))


if __name__ == "__main__":
    demo()