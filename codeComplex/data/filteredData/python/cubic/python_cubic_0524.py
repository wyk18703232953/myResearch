import math
import random


def ncr(n, r, p):  # using Fermat's little theorem
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    return list(set(l))


def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p
    return res


def prefix_sum(arr):
    r = [0] * (len(arr) + 1)
    for i, el in enumerate(arr):
        r[i + 1] = r[i] + el
    return r


def divideCeil(n, x):
    if n % x == 0:
        return n // x
    return n // x + 1


def solve_single(a_str, b_str):
    a = a_str
    b = b_str
    ans = [a]
    a_list = list(a)
    b1 = b[:]
    b_list = list(b)
    if len(a_list) < len(b_list):
        a_list.sort(reverse=True)
        return ''.join(a_list)
    arr = [0] * 10
    for ch in a_list:
        arr[int(ch)] += 1
    f = 0
    for chota in range(len(b_list)):
        arr1 = arr[:]
        temp = b_list[:chota]

        for h in range(chota):
            if arr1[int(b_list[h])] <= 0:
                f = 1
                break
            else:
                arr1[int(b_list[h])] -= 1
        if f == 1:
            break
        for j in range(int(b_list[chota]) - 1, -1, -1):
            if arr1[j] > 0:
                temp.append(str(j))
                arr1[j] -= 1
                break
        for h in range(9, -1, -1):
            if arr1[h] > 0:
                temp += [str(h)] * arr1[h]
        ans.append(''.join(temp))
    for i in ans:
        if i <= b1:
            m = i
            break
    a_list.sort(reverse=True)
    ans.append(''.join(a_list))
    for i in ans:
        if i <= b1:
            if i > m:
                m = i
    return m


def generate_test_case(n):
    # n controls the length of string a; b is chosen so that |b| is either |a| or |a|+1
    length_a = max(1, n)
    a = ''.join(str(random.randint(0, 9)) for _ in range(length_a))
    # Ensure b is a random integer with length_a or length_a+1
    # Make b not too small: at least same order as a
    if random.choice([True, False]):
        # same length
        min_b = 10 ** (length_a - 1)
        max_b = 10 ** length_a - 1
    else:
        # maybe larger length
        min_b = 10 ** (length_a - 1)
        max_b = 10 ** length_a - 1
    b_int = random.randint(min_b, max_b)
    b = str(b_int)
    return a, b


def main(n):
    random.seed(0)
    a, b = generate_test_case(n)
    result = solve_single(a, b)
    print(result)


if __name__ == "__main__":
    # Example: run with n = 10
    main(10)