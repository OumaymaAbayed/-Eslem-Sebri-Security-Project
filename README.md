# 🚗🔐 Encrypted Scraping & Analysis of Tayara.tn Car Listings

## 🧠 Project Overview
This project demonstrates a secure data pipeline for scraping, encrypting, and analyzing car sales listings from the Tunisian marketplace [Tayara.tn](https://www.tayara.tn/).

👩‍💻 **By:** Oumayma Abayed & Eslem Sebri  
📅 **Date:** May 18, 2025  
🏫 **Course:** Information Assurance and Security

---

## 🗂️ Table of Contents
- [🚀 Goals](#-goals)
- [🛠️ Tech Stack](#-tech-stack)
- [🔎 Pipeline](#-pipeline)
- [🔐 Encryption](#-encryption)
- [🖥️ Interface Modes](#-interface-modes)
- [📸 Screenshots](#-screenshots)
- [📁 Project Structure](#-project-structure)
- [📌 How to Run](#-how-to-run)
- [📝 License](#-license)

---

## 🚀 Goals
- Scrape real-world car listings data from Tayara.tn.
- Structure and clean unstructured web data.
- Encrypt the dataset to ensure confidentiality. 🔐
- Provide a graphical interface for users to filter and analyze data securely.

---

## 🛠️ Tech Stack
- 🐍 Python
- 🧪 Pandas, NumPy
- 🕸️ Selenium (for dynamic web scraping)
- 🔒 cryptography (Fernet AES encryption)
- 🖼️ Tkinter (for GUI)

---

## 🔎 Pipeline

1. **Web Scraping** – Extract listings data from the first 18 pages of Tayara.tn 🚘
2. **Data Cleaning** – Remove inconsistencies and store as CSV 🧼
3. **Encryption** – Encrypt dataset using AES-based Fernet algorithm 🔐
4. **Interface** – Visual and filterable GUI for secure interaction 📊

---

## 🔐 Encryption
- A symmetric key is generated (or loaded from `encryption.key`) 🔑
- Dataset (`tayara_vehicles_cleaned.csv`) is encrypted into `tayara_vehicles_cleaned_encrypted.csv`
- Ensures confidentiality and safe handling of scraped data ✅

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
encrypted = fernet.encrypt(data)


For the final deliverables, the executable file was too large to submit directly. Therefore, we uploaded our files to a shared drive folder: (https://drive.google.com/drive/folders/17VJ_wtALpBF6FYjkOWcrJBe7_sE3U0wR?usp=drive_link)

You can find the executable version in: ``` D3/ main exee/ dist```
