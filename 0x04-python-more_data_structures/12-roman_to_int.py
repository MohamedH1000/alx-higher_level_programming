#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return(0)
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    sss = 0
    for a in range(len(roman_string)):
        if a > 0 and r[roman_string[a]] > r[roman_string[a-1]]:
            sss += r[roman_string[a]] - 2 * r[roman_string[a-1]]
        else:
            sss += r[roman_string[a]]
    return(sss)
