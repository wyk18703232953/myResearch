from collections import Counter

class Node:
    def __init__(self, val):
        self.val = val
        self.forw = set()
        self.cou = 0

    def __str__(self):
        return f'{self.val} {self.forw} {self.cou}'

def main(n):
    # Generate deterministic input of size n
    # Original first line: n
    # Original second line: n-1 integers in [1, n], here we generate:
    # x_c = (c % (c-1)) + 1 for c from 2 to n
    arr = [Node(i) for i in range(1, n + 1)]
    c = 2
    for c in range(2, n + 1):
        x = (c % (c - 1)) + 1
        arr[x - 1].forw.add(c)

    dct = Counter()
    lst = [1]
    while len(lst):
        fl = 0
        for i in arr[lst[-1] - 1].forw:
            lst.append(i)
            fl = 1
            break
        if fl:
            arr[lst[-2] - 1].forw.remove(i)
        if not fl:
            if arr[lst[-1] - 1].cou == 0:
                arr[lst[-1] - 1].cou = 1
            dct[arr[lst[-1] - 1].cou] += 1
            k = arr[lst.pop() - 1].cou
            if len(lst):
                arr[lst[-1] - 1].cou += k

    y = 1
    out = []
    for _ in range(n):
        while not dct[y]:
            y += 1
        dct[y] -= 1
        out.append(str(y))
    # print(" ".join(out))
    pass
if __name__ == "__main__":
    main(10)