# 🔐 Cryptography Algorithms Implementation

A Python-based cryptography project that demonstrates the implementation of commonly used cryptographic algorithms including **AES**, **RSA**, and **SHA**. This project provides a simple command-line interface for encryption, decryption, hashing, and file integrity verification.

---

## 📌 Features

* AES-256 Encryption and Decryption
* RSA-2048 Public Key Encryption
* SHA Hashing (MD5, SHA-1, SHA-256, SHA-512)
* File Encryption using AES
* File Integrity Verification using SHA-256
* Random AES Key Generation
* RSA Public and Private Key Generation
* Interactive Command-Line Interface (CLI)

---

## 🛠️ Technologies Used

* Python 3.x
* PyCryptodome
* hashlib
* Git & GitHub

---

## 📁 Project Structure

```text
Cryptography-Algorithms-Implementation/
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── demo/
│   ├── sample.txt
│   ├── sample.enc
│   └── sample_decrypted.txt
│
├── keys/
│   ├── aes_key.bin
│   ├── private.pem
│   └── public.pem
│
├── screenshots/## 📷 Screenshots

### Main Menu

![Main Menu](screenshots/01_main_menu.png)

### AES Encryption

![AES Encryption](screenshots/02_aes_demo.png)

### RSA Encryption

![RSA Encryption](screenshots/03_rsa_demo.png)

### SHA Hashing

![SHA Hashing](screenshots/04_sha_demo.png)
│
├── src/
│   ├── aes/
│   │   └── aes_encrypt.py
│   ├── rsa/
│   │   └── rsa_encrypt.py
│   └── sha/
│       └── sha_hash.py
│
├── test_file.py
└── test_hash.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<hamsikamatamsetti-git>/Cryptography-Algorithms-Implementation.git
```

Go to the project folder:

```bash
cd Cryptography-Algorithms-Implementation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the main application:

```bash
python main.py
```

---

## 🔒 Supported Algorithms

### AES-256

* Symmetric encryption
* CBC mode
* PKCS7 padding
* Random IV generation

### RSA-2048

* Public key encryption
* OAEP padding
* Public/Private key generation

### SHA

* MD5
* SHA-1
* SHA-256
* SHA-512
* File SHA-256 hashing

---

## 📷 Sample Output

```text
===========================================
Cryptography Algorithms Implementation
===========================================

1. AES Encryption
2. RSA Encryption
3. SHA Hashing
4. Exit
```

---

## 📚 Learning Outcomes

* Cryptography fundamentals
* Symmetric and asymmetric encryption
* Hashing algorithms
* File encryption
* Secure key management
* Python package organization
* Git and GitHub workflow

---

## 🚀 Future Improvements

* AES-GCM authenticated encryption
* Digital signatures using RSA
* Hybrid encryption (AES + RSA)
* Graphical User Interface (GUI)
* Secure password manager
* File integrity checker for directories

---

## 👩‍💻 Author

**Hamsika Matamsetti**

Cybersecurity and Python Enthusiast
GitHub: https://github.com/hamsikamatamsetti-git
---

## 📄 License

This project is licensed under the MIT License.
