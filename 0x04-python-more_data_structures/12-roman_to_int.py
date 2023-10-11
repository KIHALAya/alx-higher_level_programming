#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string is not None:
        thousands_dict = {'M': 1000, 'MM': 2000, 'MMM': 3000}
        hundreds_dict = {'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500,
                         'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900}
        tens_dict = {'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40,
                     'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90}
        units_dict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4,
                      'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}

        dict_list = [thousands_dict, hundreds_dict, tens_dict, units_dict]
        keys_found = []

        for dictionary in dict_list:
            longest_key = ""
            for key in dictionary:
                if key in roman_string and len(key) > len(longest_key):
                    longest_key = key
            if longest_key:
                keys_found.append(longest_key)

        decimal = 0
        for key in keys_found:
            for dictionary in dict_list:
                if key in dictionary:
                    decimal += dictionary[key]
        return (decimal)

    else:
        return (0)
