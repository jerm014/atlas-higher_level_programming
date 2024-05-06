#!/usr/bin/python3
if __name__ != '__main__':
    exit


def roman_to_int(roman_string):
    roman = {"III": 3, "XXX": 30, "CCC": 300, "MMM": 3000, "II": 2, "XX" : 20, \
            "CC": 200, "MM": 2000, "IV" : 4, "IX" : 9, "XL": 40, "XC": 90, \
            "CD": 400, "CM" : 900, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, \
            "D": 500, "M": 1000}
    res = 0

    if roman_string != "" and isinstance(roman_string, str):
        for i in roman:
            if roman_string.find(i) != -1:
                roman_string = roman_string.replace(i, "")
                res += roman[i]
    return res
