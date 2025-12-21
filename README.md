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
