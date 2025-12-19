#!/usr/bin/env python3

class SecurePlant:
    """
    A plant class that protects its data using encapsulation.
    Ensures height and age are never negative.
    """

    def __init__(self, name: str, height: int, age: int):
        """Initializes the plant with protected attributes."""
        self.name = name
        # We use the setters immediately to validate initial data
        self.set_height(height)
        self.set_age(age)

    # --- Height Management ---
    def get_height(self) -> int:
        """Safe way to access height[cite: 217]."""
        return self._height

    def set_height(self, value: int):
        """Controlled way to modify height with validation[cite: 216, 218]."""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]") [cite: 230]
            print("Security: Negative height rejected") [cite: 231]
            # If initialization fails, we set a safe default
            if not hasattr(self, '_height'):
                self._height = 0
        else:
            self._height = value
            if hasattr(self, '_height'): # Only print 'OK' if updating, not during __init__
                 print(f"Height updated: {value}cm [OK]") [cite: 228]

    # --- Age Management ---
    def get_age(self) -> int:
        """Safe way to access age[cite: 217]."""
        return self._age

    def set_age(self, value: int):
        """Controlled way to modify age with validation[cite: 216, 219]."""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
            if not hasattr(self, '_age'):
                self._age = 0
        else:
            self._age = value
            if hasattr(self, '_age'):
                print(f"Age updated: {value} days [OK]") [cite: 229]

    def __str__(self):
        """Returns the current status of the plant."""
        return f"Current plant: {self.name} ({self._height}cm, {self._age} days)" [cite: 232]


if __name__ == "__main__":
    print("== Garden Security System") [cite: 226]
    
    # 1. Create a plant
    rose = SecurePlant("Rose", 20, 25) [cite: 227]
    
    # 2. Valid updates
    rose.set_height(25)
    rose.set_age(30)
    
    # 3. Invalid update (Negative value)
    rose.set_height(-5)
    
    # 4. Final status
    print(rose)