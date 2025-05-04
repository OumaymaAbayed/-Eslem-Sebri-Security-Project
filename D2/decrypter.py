from cryptography.fernet import Fernet
import os

# File paths
key_file_path = "encryption.key"
encrypted_file_path = "tayara_vehicles_encrypted.csv"
decrypted_output_path = "tayara_vehicles_decrypted.csv"

# Check if necessary files exist
if not os.path.exists(key_file_path):
    print(f"❌ Encryption key file '{key_file_path}' not found.")
    exit()

if not os.path.exists(encrypted_file_path):
    print(f"❌ Encrypted file '{encrypted_file_path}' not found.")
    exit()

# Load the encryption key
with open(key_file_path, "rb") as key_file:
    key = key_file.read()

# Initialize Fernet
fernet = Fernet(key)

# Read the encrypted file
with open(encrypted_file_path, "rb") as enc_file:
    encrypted_data = enc_file.read()

# Decrypt the data
try:
    decrypted_data = fernet.decrypt(encrypted_data)
except Exception as e:
    print(f"❌ Decryption failed: {e}")
    exit()

# Save the decrypted data
with open(decrypted_output_path, "wb") as dec_file:
    dec_file.write(decrypted_data)

print(f"✅ File decrypted successfully and saved as '{decrypted_output_path}'.")
