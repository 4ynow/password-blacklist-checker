# Password Blacklist Checker

A quick Python script that checks whether a given password appears in a wordlist of commonly used passwords.

## How it works

- Reads a text file (`wordlist.txt`) containing one password per line.
- Loads all passwords into a Python set for instant lookup.
- Asks the user for a password.
- Reports whether the password is found in the wordlist.

## How to run

1. Clone or download this repository.
2. Place a wordlist file named `wordlist.txt` in the same folder as the script.
3. Run the script:

        python password_checker.py

## Wordlist

A wordlist is not included. You can use a small custom wordlist or any public wordlist. The script also contains a few example passwords to test with.

## Example

        Password: 123456
        Password is really common.

---

Part of my Python learning journey. Open‑source, modify freely.
