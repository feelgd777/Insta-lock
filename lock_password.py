from cryptography.fernet import Fernet
from getpass import getpass

if __name__ == "__main__":
    print("This script will encrypt your Instagram password.")
    print("Enter the password.")
    print("For real use later, you will run it again and enter your REAL IG password.\n")

    pw = getpass("Enter password to lock (input hidden): ").strip()

    if not pw:
        print("No password entered. Abort.")
        raise SystemExit(1)

    # Generate a key (this goes to your friend)
    key = Fernet.generate_key()
    f = Fernet(key)

    # Encrypt the password
    token = f.encrypt(pw.encode("utf-8"))

    print("\n========== OUTPUT ==========\n")

    print("DECRYPTION KEY (give this to your friend, then delete your copy):\n")
    print(key.decode("utf-8"))

    print("\nENCRYPTED TOKEN (paste this into reveal_password.py):\n")
    print(token.decode("utf-8"))

    print("\n============================\n")
    print("NEXT STEPS:")
    print("  1) Copy the ENCRYPTED TOKEN into reveal_password.py as ENCRYPTED_TOKEN.")
    print("  2) For a real lock later: send the KEY to your friend and delete it locally.")
    print("  3) When testing now, just keep the key locally to make sure decryption works.")
