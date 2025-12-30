import bisect
import random
import string

ls2int = lambda ls: int(''.join(map(str, ls)))


def candidates(digs, num):
    if not digs:
        return [[]]

    res = []
    i = bisect.bisect_left(digs, num[0])

    # lead with same digit
    if num[0] in digs:
        for suffix in candidates(digs[:i] + digs[i + 1 :], num[1:]):
            res.append([digs[i]] + suffix)

    # lead with next smallest digit:
    if i > 0:
        i -= 1
        res.append([digs[i]] + list(reversed(digs[:i] + digs[i + 1 :])))

    return res


def solution(a, b):
    digits = [int(x) for x in sorted(a)]
    ceiling = [int(x) for x in b]

    assert len(digits) <= len(ceiling), "solution does not exist"
    if len(digits) < len(ceiling):
        return ls2int(digits[::-1])
    return max(ls2int(ls) for ls in candidates(digits, ceiling))


def gen_test_data(n):
    # n controls the length of string a
    # length of b is either n or n+1, to ensure many valid cases
    if n <= 0:
        n = 1

    # generate a: n random digits, avoid all zeros to keep non-trivial
    a_digits = [random.choice(string.digits) for _ in range(n)]
    # avoid all leading zeros if possible
    if all(d == '0' for d in a_digits):
        a_digits[0] = '1'
    a = ''.join(a_digits)

    # decide length of b
    len_b = n if random.random() < 0.7 else n + 1

    # generate b as a random number with len_b digits, not smaller than 10^(len_b-1)
    first_digit = random.randint(1, 9)
    other_digits = [random.randint(0, 9) for _ in range(len_b - 1)]
    b = str(first_digit) + ''.join(str(d) for d in other_digits)

    return a, b


def main(n):
    a, b = gen_test_data(n)
    try:
        ans = solution(a, b)
        print(a)
        print(b)
        print(ans)
    except AssertionError:
        # If generated data violates len(a) <= len(b), regenerate once
        a, b = gen_test_data(n)
        ans = solution(a, b)
        print(a)
        print(b)
        print(ans)


if __name__ == "__main__":
    main(5)