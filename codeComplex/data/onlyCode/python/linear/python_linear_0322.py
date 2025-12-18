def solve():
    n = int(input())
    a_dicts = [{}, {}]
    for j in range(2):
        for i in range(n):
            x = input()
            if x in a_dicts[j]:
                a_dicts[j][x] += 1
            else:
                a_dicts[j][x] = 1
            if x not in a_dicts[1 - j]:
                a_dicts[1 - j][x] = 0
    c = 0
    for k in a_dicts[0]:
        c += abs(a_dicts[0][k] - a_dicts[1][k])
    return c // 2

print(solve())