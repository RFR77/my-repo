#!/usr/bin/env python3

dateWT = input("Enter the date needed for input (mm/dd/yy): ")

currWt = float(input("Enter current weight: "))
#Need to make sure this number less then 300
if currWt < 300:
    print("XXX")
print("Please enter a weight less then 300.")

#f = open('output', 'w')
#f.write(str(dateWT)  + '\n')
#f.write(str(currWt)  + '\n')
#f.close()

#print("On",dateWT,"my weight was",currWt,".")
