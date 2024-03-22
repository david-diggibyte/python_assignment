def stack_cubes(t, test_cases):
    results = []

    for i in range(t):
        n = test_cases[i][0]
        l = test_cases[i][1]
        b = []
        while len(l) > 0:
            if l[-1] > l[0]:
                b.append(l.pop(-1))
            else:
                b.append(l.pop(0))
        c = b.copy()
        b.sort(reverse=True)
        if b == c:
            results.append('Yes')
        else:
            results.append('No')

    return "\n".join(results)

