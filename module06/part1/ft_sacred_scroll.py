# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sacred_scroll.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/15 09:33:55 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/15 17:59:16 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from alchemy.elements import create_air, create_earth, create_fire, create_water
import alchemy

if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===")
    print("\nTesting direct module accress:")
    print(f"alchemy.elements.create_fire(): {create_fire()}")
    print(f"alchemy.elements.create_water(): {create_water()}")
    print(f"alchemy.elements.create_earth(): {create_earth()}")
    print(f"alchemy.elements.create_air(): {create_air()}")
    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")