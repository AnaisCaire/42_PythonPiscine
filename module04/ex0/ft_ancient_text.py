
def data_recovery():
    """
    Data recovery tester
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print("\nAccessing Storage Vault: ancient\_fragment.txt")

        data = open("ancient_fragment.txt", "r")
        print("Connection established...")

        print("\nRECOVERY DATA:")
        print(data.read())

        print("\nData recovery completed")
        print("Disconnecting storage unit...")
        data.close() # not necessary
    except FileNotFoundError:
        print("Error: Storage vault not found. Run data generator first.")

if __name__ == "__main__":
    data_recovery()