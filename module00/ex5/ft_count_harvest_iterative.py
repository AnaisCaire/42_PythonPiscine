# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 15:24:45 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 15:07:26 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days+1):
        print(f"Days {i}")
    print("Harvest Time!")
