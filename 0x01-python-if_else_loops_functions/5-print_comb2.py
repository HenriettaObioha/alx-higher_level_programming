#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        pint("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
