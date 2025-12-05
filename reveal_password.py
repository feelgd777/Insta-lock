from cryptography.fernet import Fernet

# STEP 1: paste the ENCRYPTED TOKEN from lock_password.py here
ENCRYPTED_TOKEN = "gAAAAABpMjy6wby_97LJBdqURmJcV40jl1h7djA59DimOc6UHb54IuATjHag60gG1rCbyJddFpcIu5CBbavJIgeuE5A1ctPLAg=="

def main():
    key_str = input("Enter decryption key you got from your friend: ").strip()

    try:
        f = Fernet(key_str.encode("utf-8"))
        pw = f.decrypt(ENCRYPTED_TOKEN.encode("utf-8")).decode("utf-8")
    except Exception as e:
        print("\n[!] Decryption failed. Wrong key or corrupted token.")
        return

    print("\nDECRYPTED PASSWORD:")
    print(pw)
    print("\nUse it to log in, then close this window.\n")

if __name__ == "__main__":
    main()

# STEP 2: run the script and paste the encription key