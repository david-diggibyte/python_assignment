def merge_the_tools(s, k):
    result_list = []
    result = ""
    for i, c in enumerate(s, 1):
        if not c in result:
            result += c
        if i % k == 0:
            result_list.append(result)
            result = ""
    return "\n".join(result_list)


