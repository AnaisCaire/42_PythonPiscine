# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 15:31:30 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 15:17:09 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(day):
        if (day > days):
            print("Harvest time!")
            return
        else:
            print("Days: ", day)
            helper(day + 1)
    helper(1)
