#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return None
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman_keys = list(roman.keys())
    count = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman_keys:
            if roman_string[i] == roman_keys[0]:
                if i < len(roman_string) - 1 and \
                  roman_string[i + 1] != roman_keys[0]:
                    count -= roman[roman_string[i]]
                else:
                    count += roman[roman_string[i]]
            else:
                count += roman[roman_string[i]]
        else:
            return None
    return count
