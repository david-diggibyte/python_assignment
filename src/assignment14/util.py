def calculating_happiness(array, set_a, set_b):
    happiness = 0
    for i in array:
        if i in set_a:
            happiness += 1
        elif i in set_b:
            happiness -= 1
    return happiness
