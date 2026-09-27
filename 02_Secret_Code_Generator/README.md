# Secret Code Generator (Caesar Cipher)

> **Quild Build Module**  
> **Author:** Penugonda Manoj Mithra  
> **Email:** penugondamanojmithra@gmail.com  
> **Internship:** Python Programming at [VaultofCodes.in](https://vaultofcodes.in)

---

## 📌 Project Overview

The **Secret Code Generator** is a Python utility that implements the Caesar Cipher—one of the earliest and most widely known encryption techniques. It enables users to securely transform sensitive plaintext messages into obfuscated ciphertext using a numeric shift key, and symmetrically decode ciphertext back to original plaintext using the corresponding inverse shift.

---

## 🧮 How It Works (Algorithmic Logic)

The Caesar Cipher performs a substitution where each letter in the plaintext is shifted a fixed number of positions down or up the alphabet.

- **Encoding Formula:**  
  $$E_n(x) = (x + n) \pmod{26}$$
- **Decoding Formula:**  
  $$D_n(x) = (x - n) \pmod{26}$$

Where:
- $x$ is the character index (0 for 'A'/'a' through 25 for 'Z'/'z').
- $n$ is the numeric shift offset chosen by the user.
- Character casing (uppercase vs. lowercase) is strictly preserved using ASCII base offsets (`ord('A')` / `ord('a')`).
- Non-alphabetic symbols (numbers, punctuation, whitespace) are passed through unaltered.

---

## ✨ Key Features

- **Bidirectional Transformation:** Seamlessly switch between encoding and decoding.
- **Dynamic Shift Value:** Accepts any integer shift value (positive shifts, custom offsets).
- **Preserved Formatting:** Whitespace, numbers, and punctuation are untouched.
- **Robust Input Handling:** Graceful exception handling for non-integer shift inputs.
- **Lightweight & Portable:** Uses pure native Python without external dependencies.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.x
- **Dependencies:** None (Pure Python standard library / built-ins `ord`, `chr`)

---

## 🚀 How to Run

1. Navigate to the project directory:
   ```bash
   cd 02_Secret_Code_Generator
   ```

2. Run the script:
   ```bash
   python secret_code_generator.py
   ```

3. Select `1` to encode a message, `2` to decode a message, or `3` to exit.

---

## 📊 Sample Output & Execution

Below is an execution screenshot demonstrating menu navigation, message encoding, and decoding:

### CLI Execution
![Secret Code Generator Output](../assets/secret_code_generator/cipher_cli_execution.png)

---

## 📂 Source File Structure

```
02_Secret_Code_Generator/
├── secret_code_generator.py    # Main program source code
└── README.md                   # Project documentation
```
