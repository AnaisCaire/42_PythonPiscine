# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/27 21:55:07 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/28 10:31:46 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def secure_valut():
    print("=== CYBER ARCHIVES VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    with open("classified_data.txt", "r") as data:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        for line in data:
            print(line.strip())

    with open("security_protocols.txt", "r") as data:
        print("\nSECURE PRESERVATION:")
        for l in data:
            print(l)

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")
    

if __name__ == "__main__":
    secure_valut()
