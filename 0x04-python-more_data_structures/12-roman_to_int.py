#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = roman_string
    if type(rom) == str and rom is not None:
        sub_rom = ["IV", "IX", "XL", "XC", "CD", "CM"]
        found = []
        total = 0
        rom_numbers = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        for sub_num in sub_rom:
            if sub_num in rom:
                found.append(sub_num)
                rom = "".join(rom.split(sub_num))

# add the found sub roms and save in total ##
        for f in found:
            for key in rom_numbers:
                if f == key:
                    total += rom_numbers[key]

        new_list = list(rom)
        for r in new_list:
            for key in rom_numbers:
                if r == key:
                    total += rom_numbers[key]
        return total
    else:
        return 0
