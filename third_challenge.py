def get_consonant_value(c):
    return ord(c) - ord('a') + 1

def highest_consonant_value(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0

    for char in s:
        if char in consonants:
            current_value += get_consonant_value(char)
            max_value = max(max_value, current_value)
        else:
            current_value = 0

    return max_value


