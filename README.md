# 42_PythonPiscine
los 11 modulos de python

## Module 01:

# Ex 4
the magic tags:
1. the Getter: @property
   Make a method read-only
   uses the underscore: to make the variables private
   ex: self._height
3. the Setter: @<name>.setter
   Makes a Security Guard to run before changing a variable
   

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


taying "open" indefinitely
