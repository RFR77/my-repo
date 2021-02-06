#!/usr/bin/env python3
f = open("5-57.txt", "r", encoding = "ISO-8859-1")
rd = f.read()
lst = rd.split(" ")
for x in rd:
    lst.append(x)
print(lst)

