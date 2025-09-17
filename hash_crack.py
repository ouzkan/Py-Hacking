import hashlib

SUPPORTED_ALGOS=["md5","sha1","sha224","sha256","sha512"]

def crack_hash(hash_to_crack,wordlist_file):
    print("[+] Starting multi-hash cracking...")
    print(f"[+] Target hash: {hash_to_crack}\n")
    print(f"[+] Wordlist file: {wordlist_file}\n")

    try:
        with open(wordlist_file,"r",encoding="utf-8",errors="ignore") as file:
            for line in file:
                password=line.strip()
                if not password:
                    continue

                for algo in SUPPORTED_ALGOS:
                    hash_obj=hashlib.new(algo)
                    hash_obj.update(password.encode('utf-8'))
                    generated_hash=hash_obj.hexdigest()

                    if generated_hash==hash_to_crack.lower():
                        print(f"[SUCCESS] Password found!")
                        print(f"Algorithm: {algo.upper()}")
                        print(f"Password: {password}")
                        return (algo, password)
        print("[FAILED] Password not found in the provided wordlist.")
        return None

    except FileNotFoundError:
        print("[ERROR] Wordlist file not found!")
        return None
    
def main():
    print("*********** Multi-Algorithm Hash Cracker ***********")

    target_hash=input("Enter the hash to crack: ").strip()
    wordlist_path=input("Enter the path to your wordlist file: ").strip()

    crack_hash(target_hash,wordlist_path)
if __name__=="__main__":
    main()