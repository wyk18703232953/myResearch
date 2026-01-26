import math

def core_algorithm(a, b, l):
    t = [[-1, 0] for _ in range(100001)]
    for i in range(a):
        if t[l[i]][0] != -1:
            return 0
        t[l[i]][0] = 3
    s = math.inf
    for i in range(a):
        idx = l[i] & b
        if t[idx][0] != -1:
            if idx != l[i] and t[idx][0] != 1:
                t[idx] = [1, min(2, t[idx][1] + 1)]

        else:
            t[idx] = [2, 1]
    for i in range(a):
        idx = l[i] & b
        if t[idx][1] != 0 and t[idx][0] == 1:
            s = min(s, t[idx][1])
    if s == math.inf:
        return -1

    else:
        return s

def generate_inputs(n):
    if n <= 0:
        n = 1
    a = min(n, 100000)
    b = (n * 12345) ^ (n // 2)
    l = [(i * 37 + (n % 100)) % 100000 for i in range(a)]
    return a, b, l

def main(n):
    a, b, l = generate_inputs(n)
    result = core_algorithm(a, b, l)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)