def change_string(string, position, character):
    result = string[:position] + character + string[position+1:]
    return result