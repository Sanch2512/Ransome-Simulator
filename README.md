🛡️ Ransomware Simulator 
🔐

A simple educational simulator that demonstrates the behavior of ransomware in a safe environment. It encrypts a test file and generates a ransomware note, mimicking a real-life ransomware attack — without causing actual harm to your system.


⚠️ Disclaimer: This project is for educational purposes only. Do not deploy or distribute it in any harmful context.


🚨 Problem Statement
Ransomware attacks are one of the most dangerous cybersecurity threats today. They work by:

Infecting a system,

Encrypting user files, and

Demanding ransom to unlock access.

Understanding how ransomware behaves can help in developing better defense strategies. However, practicing this in the real world is risky. So this project offers a simulated environment to learn how ransomware works safely.


💡 Project Solution

This ransomware simulator is designed as a safe, controlled, and educational tool to demonstrate how ransomware works — without harming any real data. Here’s how the solution unfolds:

🔹 1. Test File Creation
A mock text file (textfile.txt) is programmatically created to simulate a real user's document or data. This represents files typically targeted by real ransomware attacks.

🔹 2. AES-Based Encryption
The simulator uses Advanced Encryption Standard (AES) — a symmetric encryption technique — to encrypt the test file using a randomly generated secret key. This ensures the file becomes unreadable unless decrypted using the same key. The key is saved separately in a secret.key file for future decryption if needed.

🔹 3. Ransom Note Generation
A realistic-looking ransom note is automatically generated (Look.txt) in the same directory. It simulates what a real victim might see — a message demanding payment in exchange for decryption, meant purely for visual and learning purposes.

🔹 4. Safety Assured
This simulator does not modify or harm actual user files on your machine. It only works within the controlled folder and is completely safe for educational use, penetration testing demos, or security awareness training.

🔹 5. Visibility of Impact
All encrypted files and the ransom message can be found in the project folder, allowing observers to visually inspect the process and understand how encryption-based ransomware typically operates.



🧰 Tools & Technologies Used

🐍 Python 3.13 – Main programming language

🔐 Fernet (from cryptography) – For symmetric AES encryption

📄 File Handling in Python – To simulate encryption & note creation

🖥️ Windows VM – Project runs inside a virtual machine for safety

🧪 VS Code – For development and testing

📎 Command Line Interface – To execute the script manually


🗂️ Repository Structure

bash
Copy
Edit
📦 ransomemess/
│
├── 📁 env/                    # Python environment (virtual)
├── 📁 img/
│   └── RansomwareSimm.png    # Diagram or illustration (optional use)
│
├── 🔑 secret.key              # Generated key for encryption/decryption
├── 📜 rnco.py                 # Main script – ransomware simulator
├── 📝 README.md               # Project documentation
├── 🧾 SECURITY.md             # Responsible disclosure & security notes
├── 📄 Look.txt                # Test file (pre-encryption)
├── 📄 textfile.txt            # Another file to test encryption
├── 📢 note.txt                # Ransom note generated
└── ℹ️  info_files...          # Other related files


🧪 How to Run
Navigate to the project folder:

bash
Copy
Edit
cd C:/cybersecurity/ransomemess


Run the script:

bash
Copy
Edit
& "C:/Program Files/Python313/python.exe" rnco.py
Check for:

Encrypted file (same name, but unreadable).

A new note.txt file with the ransom message.

📞 Contact Me
💁‍♀️ Sanchita Thakur
📬 Email: monetc724@gmail.com
🔗 LinkedIn: linkedin.com/in/claude-monet-96275b294
💻 GitHub: github.com/Sanch2512

❤️ Acknowledgments
This simulator was made as part of a cybersecurity awareness and learning initiative. Thanks to the community for inspiring ethical hacking education.

