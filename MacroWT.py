#!/usr/bin/env python3

dateWT = input("Enter the date needed for input (mm/dd/yy): ")
currWt = float(input("Enter current weight: "))

f = open('output', 'w')
f.write(str(dateWT)  + '\n')
f.write(str(currWt)  + '\n')
f.close()

print("On",dateWT,"my weight was",currWt,".")
