# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_stream_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 12:49:09 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/27 21:53:05 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def treechannels():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"[ STANDARD ] Archive status from {id}: {status}.\n")
    sys.stderr.write("[ ALERT ] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[ STANDARD] Data transmission complete\n")


if __name__ == "__main__":
    treechannels()