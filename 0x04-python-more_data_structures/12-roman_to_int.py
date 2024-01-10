def roman_to_int(roman):
    if not isinstance(roman, str) or roman is None:
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(
        rom_n[c] * (1 if rom_n[c] >= rom_n[d] else -1)
        for c, d in zip(roman, roman[1:] + '0')
    )
