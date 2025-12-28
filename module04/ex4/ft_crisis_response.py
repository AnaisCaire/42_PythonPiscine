# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_crisis_response.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/27 22:21:47 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/28 10:57:13 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def crisis_response(file_name):
    """
    How to handle crisis
    """
    print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        with open(f"{file_name}", "r") as data:
            for line in data:
                print(f"SUCCESS: Archive recovered - {line}")
            print("STATUS: Normal operations resumed")
    
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
     
def main():
    """
    Use to test function
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files = ["lost_archive.txt", "classified_vault.txt", "standard_archive.txt"]
    for file in files:
        crisis_response(file)
    print("\nAll crisis scenarios handled successfully. Archives secure.")
    

if __name__ == "__main__":
    main()
