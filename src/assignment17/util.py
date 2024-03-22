
from itertools import combinations
def calculate_probability(n, l, k):
    all_combinations = list(combinations(l, k))
    filter_combinations = filter(lambda c: 'a' in c, all_combinations)
    probability = len(list(filter_combinations)) / len(all_combinations)
    return float("{0:.3f}".format(probability))
