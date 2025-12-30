import random

def next_index(k, a, x):
    while k < len(a) and a[k] < x:
        k += 1
    return k

def main(n):
    # n: number of vertical values (vert)
    # To make it scalable, let m be proportional to n
    m = max(1, n * 2)  # for example, m = 2n

    # Generate test data:
    # vert: n random integers in [1, 1e9)
    vert = [random.randint(1, 10**9 - 1) for _ in range(n)]

    # horizontal-like data: we only actually use x2 when x1 == 1
    # generate m triples (x1, x2, y), but keep only x2 where x1 == 1
    horz = []
    for _ in range(m):
        x1 = random.randint(1, 2)  # randomly 1 or 2
        x2 = random.randint(1, 10**9 - 1)
        y = random.randint(1, 10**9 - 1)  # y is irrelevant to the logic
        if x1 == 1:
            horz.append(x2)

    vert.sort()
    horz.sort()
    vert.append(10**9)

    num = next_index(0, horz, vert[0])
    ans = len(horz) - num

    for i in range(1, len(vert)):
        num2 = next_index(num, horz, vert[i])
        t = i + len(horz) - num2
        if t < ans:
            ans = t
        num = num2

    print(ans)


if __name__ == "__main__":
    # example run with n = 5
    main(5)