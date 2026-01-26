c = 0

def backtracking(actuales, restantes, l, r, x):
    global c
    if actuales:
        s = sum(actuales)
        if l <= s <= r:
            if max(actuales) - min(actuales) >= x:
                c += 1
    if restantes:
        for i in range(len(restantes)):
            backtracking(actuales + [restantes[i]], restantes[i+1:], l, r, x)
    return 0

def main(n):
    global c
    c = 0
    if n < 1:
        return 0
    l = n
    r = 2 * n
    x = max(1, n // 3)
    difficulties = [i + 1 for i in range(n)]
    difficulties.sort()
    backtracking([], difficulties, l, r, x)
    return c

if __name__ == "__main__":
    print(main(10))