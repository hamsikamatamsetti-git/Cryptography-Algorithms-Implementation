from src.sha.sha_hash import SHAHasher

print(
    SHAHasher.file_sha256(
        "demo/sample.txt"
    )
)