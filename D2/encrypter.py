from cryptography.fernet import Fernet

# Generate a key (only run this ONCE and save the key)
key = Fernet.generate_key()

# Save the key securely
with open("encryption.key", "wb") as key_file:
    key_file.write(key)

# Initialize Fernet with the key
fernet = Fernet(key)

# Read the CSV file to encrypt
with open("tayara_vehicles.csv", "rb") as file:
    original = file.read()

# Encrypt the data
encrypted = fernet.encrypt(original)

# Save the encrypted data to a file
with open("tayara_vehicles_encrypted.csv", "wb") as enc_file:
    enc_file.write(encrypted)

print("✅ tayara_vehicles.csv has been encrypted.")