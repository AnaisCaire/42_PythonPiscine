# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 15:24:45 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/11 17:20:54 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    while (i <= days):
        print("Day ", i)
        i += 1
    if i == days + 1:
        print("Harvest time!")
