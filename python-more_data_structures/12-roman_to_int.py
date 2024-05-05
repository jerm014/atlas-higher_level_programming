#!/usr/bin/python3
if __name__ != '__main__':
    exit


def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sub = {"IV" : 4, "IX" : 9, "XL": 40, "XC": 90, "CD": 400, "CM" : 900}
    others1 = {"III": 3, "XXX": 30, "CCC": 300, "MMM": 3000}
    others2 = {"II": 2, "XX" : 20, "CC": 200, "MM": 2000}
    
    for i in range(0,len(roman_string)-2):
        # find out if there are any cases of subtraction?
        if roman_string[i: i + 1] == "IV"

