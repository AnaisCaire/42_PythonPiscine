# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 17:20:26 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/19 17:47:13 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

##the helpfull error message should not be hardcoded in the class but should be raised
class GardenError(Exception):
    """A basic error for garden problems."""
    def __init__(self, message= "Caught a garden error"):
        self.message = message
        super().__init__(message)
    pass

class PlantError(GardenError):
    """For problems with plants (inherits from GardenError)."""
    def __init__(self, message="Plant error"):
        super().__init__(message)
    pass

class WaterError(GardenError):
    """For problems with watering (inherits from GardenError)."""
    def __init__(self, message="A watering-related error occurred"):
        super().__init__(message)
    pass


def test_custom_errors():
    """Demonstrates raising and catching custom garden errors."""
    print("Custom Garden Errors Demo")

    # Testing specific errors
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    # Testing the hierarchy (Catching all)
    print("Testing catching all garden errors...")
    errors_to_test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]
    
    for err in errors_to_test:
        try:
            raise err
        except GardenError as e:
            # This demonstrates that GardenError is a parent to both
            print(f"Caught a garden error: {e}")

if __name__ == "__main__":
    test_custom_errors()