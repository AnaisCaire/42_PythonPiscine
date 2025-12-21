# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 13:39:24 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 14:42:33 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    """
    Show the total harvest of 3 days
    """
    day1 = input("Day 1 harvest: ")
    day2 = input("Day 2 harvest: ")
    day3 = input("Day 3 harvest: ")
    sum = int(day1) + int(day2) + int(day3)
    print("Total harvest: ", sum)
