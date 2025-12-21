# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 13:19:37 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 14:49:37 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_plot_area():
    """
    Calculate the plot area with the lenght and width
    """
    len: str = input("Enter lenght: ")
    wid: str = input("Enter width: ")
    print("plot area: ", int(len) * int(wid))
