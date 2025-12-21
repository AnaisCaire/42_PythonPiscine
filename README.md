# 42_PythonPiscine
los 11 modulos de python

## Module 02:

why use try, raise, except and exception ?
Because that's how you do __Defensive Programming__

# Raise:
It's a signal detection for triggering errors that python dosen't know it's a crash
for example, water level -50 is impossible in our case. 
  - You have to __raise__ a "WaterError" so the program stops.

# try/Except:
try : Show "risky" code in a try block
except: show what to do if things go wrong == log the error
  except makes the system keep working even when some of the parts fail == fault tolerance
