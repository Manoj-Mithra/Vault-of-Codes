# Vault of Codes (VOC) — Python Programming Internship

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Internship Organization](https://img.shields.io/badge/Internship-VaultofCodes.in-orange.svg)](https://vaultofcodes.in)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#-internship--academic-context)
[![Certificate](https://img.shields.io/badge/Certificate-Verified-brightgreen.svg?logo=academia)](VOC%20CERTIFICATE.pdf)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Portfolio & Project Showcase**  
> **Author:** Penugonda Manoj Mithra  
> **Email:** [penugondamanojmithra@gmail.com](mailto:penugondamanojmithra@gmail.com)  
> **Internship:** 1-Month Intensive Python Programming Internship at [VaultofCodes.in](https://vaultofcodes.in)  
> **Commencement Date:** August 5, 2025 (`05/08/2025`)

---

## 🎓 Academic Stage & Purpose of This Repository

This repository represents the software projects, modules, and technical solutions **developed by me** during a pivotal stage of my academic journey in computer science and engineering.

### Why I Developed These Projects
At this stage of my academics, my primary objective was to transition beyond theoretical classroom concepts and acquire hands-on, industry-relevant software development competencies. To achieve this, I undertook an intensive **1-Month Internship in Python Programming** offered by **Vault of Codes** ([VaultofCodes.in](https://vaultofcodes.in)), starting on **August 5, 2025**.

Through this program, I was tasked with solving real-world software engineering challenges requiring:
1. **Applied Data Structures & File Handling:** Moving from transient in-memory calculations to structured, persistent storage with JSON serialization.
2. **Data Analytics & Visualization:** Developing algorithmic aggregations and visual representations of metrics using Matplotlib.
3. **Applied Cryptography & Logic Design:** Implementing classical mathematical encryption mechanisms, cyclic ASCII transformations, and robust CLI user experiences.

---

## 📜 Verified Internship Credential

Upon successfully completing the assigned projects, code submissions, and technical assessments, I was awarded an official **Certificate of Internship Completion** by Vault of Codes.

### 👤 My Credential & Student Profile

| Information Field | My Credential Details |
| :--- | :--- |
| **Full Name** | **Penugonda Manoj Mithra** |
| **Email Address** | [penugondamanojmithra@gmail.com](mailto:penugondamanojmithra@gmail.com) |
| **University Student ID** | *Student ID Registered with University* |
| **AICTE Student ID** | *AICTE Internship Portal ID* |
| **Program Title** | 1-Month Internship in Python Programming |
| **Training Organization** | [VaultofCodes.in](https://vaultofcodes.in) (Vault of Codes) |
| **Commencement Date** | August 5, 2025 (`05/08/2025`) |
| **Certificate Signatories** | Kartik Ahlawat (Founder) & Varshita Singh (HR Manager) |
| **Official Certificate File** | 📄 [VOC CERTIFICATE.pdf](VOC%20CERTIFICATE.pdf) |

> 🔍 **Verification:** The authenticated certificate awarded to me is permanently tracked in this repository as [VOC CERTIFICATE.pdf](VOC%20CERTIFICATE.pdf). It includes a QR code linking to my verified performance metrics and assessment report.

---

## 📂 Repository Architecture

```
Vault-of-Codes/
├── 01_Personal_Expense_Tracker/       # Mini Project (Assignment 3) developed by me
│   ├── expense_tracker.py             # Complete CLI application source code
│   ├── requirements.txt               # Dependencies (matplotlib)
│   └── README.md                      # Dedicated project documentation
├── 02_Secret_Code_Generator/          # Quild Build Module developed by me
│   ├── secret_code_generator.py       # Caesar cipher implementation
│   └── README.md                      # Dedicated project documentation
├── assets/                            # Execution screenshots from my testing
│   ├── expense_tracker/
│   │   ├── execution_and_plot.png     # Terminal execution & Matplotlib chart
│   │   └── expenses_json_data.png     # Persistent expenses.json record
│   └── secret_code_generator/
│       └── cipher_cli_execution.png   # Cipher encoding/decoding run
├── DOCUMENTATION.md                   # Consolidated technical code & algorithm docs
├── VOC CERTIFICATE.pdf                # My official internship certificate
├── LICENSE                            # MIT License
└── README.md                          # Main project & credential showcase
```

---

## 🚀 Projects Developed By Me

### 1. 💰 Personal Expense Tracker (`01_Personal_Expense_Tracker`)
> **Curriculum Component:** Mini Project — Assignment 3  
> **Developed by:** Penugonda Manoj Mithra

#### Purpose & Motivation:
As a student managing day-to-day living and academic expenses, tracking financial habits and sticking to a budget is essential. I developed this application to address this need through a modular Python CLI utility that allows users to record daily expenses, categorize transactions, persist records across sessions in JSON, inspect multi-dimensional financial summaries, and visualize expense distributions graphically.

#### What I Implemented:
- **Transaction Logging:** Captures expense amount, category (e.g., Food, Transport, Entertainment, Academics), and date (defaults to current date if left empty).
- **Persistent Storage:** Built custom file I/O operations (`load_expenses()`, `save_expenses()`) interfacing with `expenses.json`, ensuring no data is lost between sessions.
- **Analytical Metrics:** Designed algorithms to compute total expenditure, category-wise breakdown, and daily chronological spending.
- **Full CRUD Management:** Allowed users to add, view, edit (updating amount, category, or date), and delete specific expense records.
- **Visual Analytics:** Integrated `matplotlib.pyplot` to generate clean pie charts representing percentage spending by category.

#### Execution Screenshots:
| CLI Execution & Analytics Visualization | Persistent JSON Storage (`expenses.json`) |
| :---: | :---: |
| ![Expense Tracker Plot](assets/expense_tracker/execution_and_plot.png) | ![Expenses JSON](assets/expense_tracker/expenses_json_data.png) |

---

### 2. 🔐 Secret Code Generator (`02_Secret_Code_Generator`)
> **Curriculum Component:** Quild Build Module  
> **Developed by:** Penugonda Manoj Mithra

#### Purpose & Motivation:
At this stage in my computer science curriculum, exploring cybersecurity and cryptography fundamentals was a key academic objective. I developed this tool to demonstrate the classical **Caesar Cipher** substitution algorithm, providing an intuitive command-line interface for encoding plaintext into encrypted ciphertext and symmetrically decoding it back.

#### What I Implemented:
- **Symmetric Encryption & Decryption:** Built `encode()` and `decode()` functions using modular arithmetic ($E_n(x) = (x + n) \pmod{26}$ and $D_n(x) = (x - n) \pmod{26}$).
- **ASCII Base Preservation:** Maintained uppercase and lowercase character integrity via `ord()` and `chr()` calculations while preserving spaces, punctuation, and digits untouched.
- **Interactive CLI & Validation:** Implemented an input validation loop that gracefully handles non-integer shift values without crashing.

#### Execution Screenshot:
| Secret Code Generator CLI Output |
| :---: |
| ![Secret Code Generator](assets/secret_code_generator/cipher_cli_execution.png) |

---

## 🛠️ Technical Competencies Demonstrated

Throughout these projects, I applied and strengthened several computer science fundamentals:

- **Programming Language:** Python 3 (Modular design, exception handling, clean code principles)
- **Data Structures:** Lists of dictionaries, hash maps, nested JSON structures
- **File Systems & I/O:** JSON serialization, structured data persistence, file checking
- **Data Analysis & Graphics:** Matplotlib plotting, dynamic percentage calculation
- **Applied Cryptography:** Modular arithmetic (`% 26`), Caesar Cipher, ASCII byte-level indexing
- **Development Workflows:** Git version control, semantic documentation, requirement management

---

## 💻 How to Run the Projects on Your Machine

### Prerequisites
Make sure Python 3.8+ is installed:
```bash
python --version
```

### Clone the Repository
```bash
git clone https://github.com/Manoj-Mithra/Vault-of-Codes.git
cd Vault-of-Codes
```

### Running Project 1: Personal Expense Tracker
```bash
cd 01_Personal_Expense_Tracker
pip install -r requirements.txt
python expense_tracker.py
```

### Running Project 2: Secret Code Generator
```bash
cd 02_Secret_Code_Generator
python secret_code_generator.py
```

---

## 📖 In-Depth Technical Documentation

For complete source code listings, function descriptions, parameters, and algorithms for both projects, please visit:  
👉 **[DOCUMENTATION.md](DOCUMENTATION.md)**

---

## 👤 Developer Profile & Contact

**Penugonda Manoj Mithra**  
- **Email:** [penugondamanojmithra@gmail.com](mailto:penugondamanojmithra@gmail.com)  
- **GitHub:** [@Manoj-Mithra](https://github.com/Manoj-Mithra)  
- **Internship Host:** [Vault of Codes](https://vaultofcodes.in)

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
