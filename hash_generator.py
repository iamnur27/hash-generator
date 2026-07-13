import hashlib

print("===== HASH GENERATOR =====")
print("1. MD5")
print("2. SHA1")
print("3. SHA256")
print("4. Generate All")

choice = input("\nChoose an option (1-4): ")

text = input("Enter text: ")

text_bytes = text.encode()

md5_hash = hashlib.md5(text_bytes).hexdigest()
sha1_hash = hashlib.sha1(text_bytes).hexdigest()
sha256_hash = hashlib.sha256(text_bytes).hexdigest()

if choice == "1":
    print("\nMD5:", md5_hash)

elif choice == "2":
    print("\nSHA1:", sha1_hash)

elif choice == "3":
    print("\nSHA256:", sha256_hash)

elif choice == "4":
    print("\nGenerated Hashes:")
    print("MD5    :", md5_hash)
    print("SHA1   :", sha1_hash)
    print("SHA256 :", sha256_hash)

else:
    print("\nInvalid option!")
