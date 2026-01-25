from collections import Counter

class Node:
    def __init__(self, val):
        self.val = val
        self.forw = set()
        self.cou = 0

    def __str__(self):
        return f'{self.val} {self.forw} {self.cou}'


def run_algorithm(n, edges):
    arr = [Node(i) for i in range(1, n + 1)]
    c = 2
    for x in edges:
        arr[x - 1].forw.add(c)
        c += 1

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
    output = []
    for _ in range(n):
        while not dct[y]:
            y += 1
        dct[y] -= 1
        output.append(y)
    return output


def main(n):
    # n is the size parameter. We map it directly to the original "n" (number of nodes/outputs).
    # We must provide exactly n-1 integers as the second line input.
    # Deterministic generation: simple modular/arithmetic pattern in [1, i]
    if n < 1:
        return []
    if n == 1:
        edges = []
    else:
        # edges length = n-1, all in [1, current_index], deterministic pattern
        edges = [(i % (i + 1)) + 1 for i in range(1, n)]  # i from 1 to n-1
    result = run_algorithm(n, edges)
    print(" ".join(map(str, result)))
    return result


if __name__ == "__main__":
    main(10)