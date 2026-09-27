# Vault of Codes (VOC) — Python Programming Internship

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Organization](https://img.shields.io/badge/Internship-VaultofCodes.in-orange.svg)](https://vaultofcodes.in)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#certificate-of-completion)
[![Certificate](https://img.shields.io/badge/Certificate-Verified-brightgreen.svg?logo=academia)](VOC%20CERTIFICATE.pdf)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Welcome to the official repository showcasing the projects, assignments, and practical implementations completed during the **Python Programming Internship** at **Vault of Codes** ([VaultofCodes.in](https://vaultofcodes.in)).

---

## 📜 Internship & Certification Showcase

This repository serves as a verified showcase of the technical coursework and software solutions developed by **Penugonda Manoj Mithra** during the **1-Month Internship in Python Programming** at **VaultofCodes.in**, commencing on **August 5, 2025**.

### 🎓 Candidate & Program Credential Overview

| Credential Detail | Verified Information |
| :--- | :--- |
| **Recipient Name** | **Penugonda Manoj Mithra** |
| **Email Address** | [penugondamanojmithra@gmail.com](mailto:penugondamanojmithra@gmail.com) |
| **Program Title** | 1-Month Internship in Python Programming |
| **Host Organization** | [VaultofCodes.in](https://vaultofcodes.in) |
| **Commencement Date** | August 5, 2025 (`05/08/2025`) |
| **Completion Status** | Successfully Completed & Certified |
| **Authentic Certificate** | 📄 [VOC CERTIFICATE.pdf](VOC%20CERTIFICATE.pdf) |

> 🎖️ **Certificate of Completion:**  
> The authenticated internship certificate has been officially awarded by **Kartik Ahlawat** (Founder) and **Varshita Singh** (HR Manager) at Vault of Codes. Authenticity and performance statistics can be inspected via the embedded QR code on the official [VOC CERTIFICATE.pdf](VOC%20CERTIFICATE.pdf).

---

## 📂 Repository Architecture

```
Vault-of-Codes/
├── 01_Personal_Expense_Tracker/       # Mini Project - Assignment 3
│   ├── expense_tracker.py             # Main CLI application
│   ├── requirements.txt               # Dependencies (matplotlib)
│   └── README.md                      # Project-specific documentation
├── 02_Secret_Code_Generator/          # Quild Build Module
│   ├── secret_code_generator.py       # Caesar cipher encoder/decoder
│   └── README.md                      # Project-specific documentation
├── assets/                            # Visual assets & screenshots
│   ├── expense_tracker/
│   │   ├── execution_and_plot.png     # CLI run & pie chart visualization
│   │   └── expenses_json_data.png     # JSON persistent data file
│   └── secret_code_generator/
│       └── cipher_cli_execution.png   # Cipher encode/decode run
├── DOCUMENTATION.md                   # Consolidated technical code & module docs
├── VOC CERTIFICATE.pdf                # Official internship certificate
├── LICENSE                            # Repository license
└── README.md                          # Comprehensive showcase documentation
```

---

## 🚀 Projects Overview

### 1. 💰 Personal Expense Tracker (`01_Personal_Expense_Tracker`)
> **Curriculum Module:** Mini Project — Assignment 3

An interactive personal finance utility that allows users to manage their daily expenses, persist records across sessions, compute analytical breakdowns, and visualize categorical expenditures graphically.

#### Key Capabilities:
- **Record Expenses:** Log entries with amount, category (e.g., Food, Transport, Entertainment), and automated or user-specified timestamps (`YYYY-MM-DD`).
- **File Persistence:** Stores records in `expenses.json` with formatting and error-safe loading.
- **Analytical Summaries:** Computes total expenditures, categorical expenditure totals, and chronological daily spending patterns.
- **CRUD Operations:** Complete capability to add, view, update (edit), and delete transactions.
- **Visual Analytics:** Generates interactive distribution pie charts using `matplotlib`.

#### Visual Output:
| CLI Execution & Analytics Visualization | Persistent JSON Storage |
| :---: | :---: |
| ![Expense Tracker Plot](assets/expense_tracker/execution_and_plot.png) | ![Expenses JSON](assets/expense_tracker/expenses_json_data.png) |

---

### 2. 🔐 Secret Code Generator (`02_Secret_Code_Generator`)
> **Curriculum Module:** Quild Build Module

A cryptographic text encryption and decryption tool based on the classic **Caesar Cipher** algorithm. It transforms sensitive plaintext into ciphered text through cyclic alphabetical shifting and restores it with exact fidelity.

#### Key Capabilities:
- **Bidirectional Transformation:** Encode plaintext messages forward and decode ciphered messages backward using user-defined shift values ($k \in \mathbb{Z}$).
- **Case & Formatting Preservation:** Retains uppercase/lowercase casing using ASCII modular arithmetic while keeping whitespace, punctuation, and numerals intact.
- **Robust Exception Handling:** Interactive terminal menu with validation protecting against non-integer shift inputs.

#### Visual Output:
| Secret Code Generator CLI Output |
| :---: |
| ![Secret Code Generator](assets/secret_code_generator/cipher_cli_execution.png) |

---

## 🛠️ Technology Stack & Skills Acquired

- **Programming Language:** Python 3 (Object & Functional Programming)
- **Data Structures:** Dictionaries, Lists, Key-Value mappings
- **File Systems & Storage:** JSON file handling (`json.load`, `json.dump`)
- **Data Visualization:** Matplotlib (`matplotlib.pyplot`)
- **Mathematics & Cryptography:** Modular arithmetic (`% 26`), Caesar Cipher, ASCII character manipulation (`ord()`, `chr()`)
- **Software Engineering Practices:** Clean modular code, exception handling, CLI UX design, Git version control

---

## 💻 Getting Started & Running the Projects

### Prerequisites
Make sure Python 3.8 or higher is installed on your system:
```bash
python --version
```

### Installation
Clone this repository and enter the workspace:
```bash
git clone https://github.com/Manoj-Mithra/Vault-of-Codes.git
cd Vault-of-Codes
```

### Running Project 1: Personal Expense Tracker
```bash
# Navigate to the project directory
cd 01_Personal_Expense_Tracker

# Install dependencies
pip install -r requirements.txt

# Run application
python expense_tracker.py
```

### Running Project 2: Secret Code Generator
```bash
# Navigate to the project directory
cd 02_Secret_Code_Generator

# Run application (No external dependencies required)
python secret_code_generator.py
```

---

## 📖 In-Depth Technical Documentation

For complete, unabridged source codes, functional tables, input/output parameters, and detailed algorithm breakdowns for both projects, please refer to:
👉 **[DOCUMENTATION.md](DOCUMENTATION.md)**

---

## 👤 Author & Contact

**Penugonda Manoj Mithra**  
- **Email:** [penugondamanojmithra@gmail.com](mailto:penugondamanojmithra@gmail.com)  
- **GitHub:** [@Manoj-Mithra](https://github.com/Manoj-Mithra)  
- **Internship Organization:** [Vault of Codes](https://vaultofcodes.in)

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
