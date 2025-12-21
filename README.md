# 42_PythonPiscine
los 11 modulos de python

## Module 02:

# Ex2
why use try, raise, except and exception ?
Because that's how you do __Defensive Programming__

## Raise:
It's a signal detection for triggering errors that python dosen't know it's a crash
for example, water level -50 is impossible in our case. 
  - You have to __raise__ a "WaterError" so the program stops.

## try/Except:
try : Show "risky" code in a try block
except: show what to do if things go wrong == log the error
  except makes the system keep working even when some of the parts fail == fault tolerance

## Example in exercice 2:
    # Testing specific errors
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

Try: "I am about to do something that might break." 
Raise: "Boom! I just broke the rule (The tomato is wilting!)" 
Except: "Don't worry, I caught the PlantError and here is the message."



# Module 03: The Resilient Garden Guardian
This module focuses on Defensive Programming and Fault Tolerance in Python. I learned how to move beyond simple logic to build a data pipeline that anticipates, signals, and recovers from failures using professional exception handling.

## Exercise 01: Built-in Safety (ZeroDivision & ValueError)
Focus: Understanding Python’s native error signals.

Concept: Learning that errors are not "crashes" but "signals." I used try and except to handle common issues like dividing by zero (empty sensor data) or converting strings to integers.

Example:

Python

try:
    avg_water = total_water / plant_count
except ZeroDivisionError:
    avg_water = 0  # Default value for empty gardens
Exercise 02: Custom Exception Hierarchies
Focus: Object-Oriented Error Design.

Concept: I built a "Family Tree" of errors using Inheritance. By creating a base class (GardenError), I can catch all specific sub-errors (like PlantError or WaterError) with a single except block.

Example:

Python

class GardenError(Exception): pass
class WaterError(GardenError): pass # Inherits from GardenError
Exercise 03: Resource Management (The Finally Block)
Focus: Guaranteed Cleanup.

Concept: I learned to use finally to ensure that critical hardware or software resources (like irrigation valves or open files) are always closed, even if the code in the try block crashes.

Example:

Python

try:
    open_irrigation_valve()
finally:
    close_irrigation_valve() # Runs even if watering fails
Exercise 04: Signaling with Raise
Focus: Explicit Error Triggering.

Concept: Instead of letting Python wait for a crash, I learned to raise my own exceptions when data violates agricultural rules (e.g., sunlight hours > 12).

Example:

Python

if sunlight > 12:
    raise SunlightError("Excessive UV exposure detected!")
Exercise 05: The Management System (Full Integration)
Focus: Encapsulation and Data Integrity.

Concept: I combined dictionaries and classes to manage complex data. I used Method Chaining (returning self) and demonstrated Error Recovery by catching parent exceptions to keep the system running after a failure.

Example:

Python

# Recovering from a specific failure
try:
    manager.water_plants()
except GardenError:
    print("System isolated the error and remains stable.")
Key Takeaway
In this module, I transitioned from writing code for the "Happy Path" (when everything works) to writing code for the "Real World" (where sensors fail, data is missing, and hardware must be protected).

## Questions:
1. When should you create your own error types instead of using Python’s
built-in ones?
when python dosen't automatically detect it's an error but in your program it should
2. How does inheritance help organize different types of
errors?
This helps provide a clearer code hierarchy making the error messages more specific and having a
stronger foundation if a problem arraises.

# Ex3

okay so the try block is not to code what might fail ! its the __Working Zone__
There should be the entire normal operation with : the protection.

concept of the "Happy path" == the execution if nothing fails is in the try block.

the role of __Finally__:
The finally block is unique because it doesn't care if the "Happy Path" finished or if you jumped to the "Error Path". It is the Cleanup Crew that ensures the system is always closed, protecting your hardware from staying "open" indefinitely
