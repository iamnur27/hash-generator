import hashlib

text = input("Enter text: ")

text_bytes = text.encode()

md5_hash = hashlib.md5(text_bytes).hexdigest()
sha1_hash = hashlib.sha1(text_bytes).hexdigest()
sha256_hash = hashlib.sha256(text_bytes).hexdigest()

print("\nGenerated Hashes:")
print("MD5    :", md5_hash)
print("SHA1   :", sha1_hash)
print("SHA256 :", sha256_hash)
