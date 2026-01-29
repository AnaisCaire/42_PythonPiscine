
def write_history():
    """
    How to write on a file/create a file
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")
        file.write("{[ ENTRY 001 ]} New quantum algorithm discovered\n")
        file.write("{[ ENTRY 002 ]} Efficiency increased by 347%\n")
        file.write("{[ ENTRY 003 ]} Archived by Data Archivist trainee\n")
        print("{[ ENTRY 001 ]} New quantum algorithm discovered")
        print("{[ ENTRY 002 ]} Efficiency increased by 347%")
        print("{[ ENTRY 003 ]} Archived by Data Archivist trainee")
        

        print("\nData inscription complete. Storage unit sealed.")
        file.close()
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError:
        print("Permissions Denied :(")
        
if __name__ == "__main__":
    write_history()
# chmod 000 new_discovery.txt -- chmod 644 new_discovery.txt