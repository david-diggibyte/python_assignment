def second_large():
    n = int(input())
    arr = list(map(int, input().split()))
    return sorted(set(arr))[-2]