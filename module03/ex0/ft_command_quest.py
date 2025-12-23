# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 13:20:11 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 15:49:00 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def command_quest():
    """
    command line interpreter
    """
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print(
            "No argument provided!"
            f"\nProgram name: {sys.argv[0]}"
            f"\nTotal arguments: {len(sys.argv)}")
    elif len(sys.argv) > 1:
        count = 1
        print(f"Program name: {sys.argv[0]}"
              f"\nArguments received: {len(sys.argv)-1}")
        for arg in sys.argv[1:]:
            print(f"Argument {(count)}: {arg}")
            count += 1
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
