# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/22 17:27:17 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/22 18:35:25 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math


def calculate_distance(pos1, pos2):
    """
    Distance between 2 coordinates in 3D (Euclidean formula)
    """
    (x1, y1, z1) = pos1
    (x2, y2, z2) = pos2
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return dist


def parse_input(str_coor):
    """
    Change the input from a string to a tuple
    """
    try:
        parsed_coor = str_coor.split(',')
        lst = []
        for i in parsed_coor:
            lst.append(int(i))
        return tuple(lst)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e}")
        return None


def main():
    """
    Function to show the Demo Simulation
    """
    print("=== Game Coordinate System ===")
    position = (10, 20, 5)
    pos0 = (0, 0, 0)
    print(f"\nPosition created: {position}")
    res = calculate_distance(pos0, position)
    print(f"Distance between {pos0} and {position}: {res:.2f}")

    coord = "3,4,0"
    print(f"\nParsing coordinates: {coord}")
    pars_res = parse_input(coord)
    if pars_res is not None:
        print(f"Parsed position: {pars_res}")
    else:
        return
    pars_dist = calculate_distance(pos0, pars_res)
    print(f"Distance between {pos0} and {pars_res}: {pars_dist:.2f}")

    inval_coor = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: {inval_coor}")
    parse_input(inval_coor)

    print("\nUnpacking demonstration:")
    print(f"Player at x={pars_res[0]}, y={pars_res[1]}, z={pars_res[2]}")
    print(f"Coordinates: X={pars_res[0]}, Y={pars_res[1]}, Z={pars_res[2]}")


if __name__ == "__main__":
    main()
