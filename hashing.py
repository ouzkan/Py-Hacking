import hashlib #Add Standart Hash Library

#This Function Creates Hashes
def generate_hashes(text):
    #Taking input and hashing every avaible hash algorithms.
    algorithms=hashlib.algorithms_guaranteed  #This one guaranteed every hash algorithms works with every OS
    results={}

    for algo in algorithms:
        try:
            hash_obj=hashlib.new(algo)
            hash_obj.update(text.encode('utf-8'))
            results[algo]=hash_obj.hexdigest()

        except Exception as e:
            results[algo]=f"Hata: {e}"
    return results

def main():
    print("*********** Pyhton Hash Generator ***********")
    text=input("Give the string that going to be hash:")
    
    print("*********** Hashing Results ***********")
    hashes=generate_hashes(text)

    for algo,hashed_text in hashes.items():
        print(f"{algo.upper()}:{hashed_text}\n")

    save_option=input("\nDo you want to save outputs? (Y/N):")
    if save_option=="Y":
        filename="hash_outputs.txt"
        with open(filename,"w",encoding="utf-8") as file:
            file.write(f"Original string:{text}\n\n")
            for algo,hashed_text in hashes.items():
                file.write(f"{algo.upper()}:{hashed_text}\n")

        print(f"[+] Hash results saved in '{filename}'")

if __name__ == "__main__":
    main()