def count_word(n, words):
    word_map = {}
    for word in words:
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1
    distinct_count = len(word_map)
    occurrences = list(word_map.values())
    output_string = f"{distinct_count}\n{' '.join(map(str, occurrences))}"
    return output_string