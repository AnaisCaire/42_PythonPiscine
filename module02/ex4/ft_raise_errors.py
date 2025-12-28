# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_errors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 09:57:55 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/21 13:03:51 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Garden checker and error messages 
    """
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
    except ValueError as e:
        print(f"Error: {e}")
        return
    try:
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too hight (max 10)")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (max 1)")
    except ValueError as e:
        print(f"Error: {e}")
        return
    try:
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    except ValueError as e:
        print(f"Error: {e}")
        return
    print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks():
    """
    Tester for function
    """
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    check_plant_health("tomato", 5, 6)
    print("\nTesting empty plant name...")
    check_plant_health(None, 5, 6)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 6)
    print("\nTesting sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print("\nAll error raising test completed!")

if __name__ == "__main__":
    test_plant_checks()