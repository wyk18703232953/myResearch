def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
               return False

        else:
            return True

    else:
        return False


def part1(n_values):
    digits = []
    new_digits = set()
    outputs = []
    for val in n_values:
        n = val
        if n in range(1, 10):
            outputs.append("1")
            outputs.append(str(n))

        else:
            while n > 0:
                digit = n % 10
                digits.append(digit)
                n = int(n / 10)
            i = 0
            for d in digits:
                new_digits.add(d * 10 ** i)
                i += 1
            if 0 in new_digits:
                new_digits.remove(0)
            outputs.append(str(len(new_digits)))
            outputs.append(" ".join(str(d) for d in new_digits))
            new_digits.clear()
            digits.clear()
    return "\n".join(outputs)


def part2(n, a):
    b = []
    for i in range(1, n + 1):
        b.append(i)
    results = []
    for l in b:
        results.append(a.index(l) + 1)
    return " ".join(str(r) for r in results)


def part3(k, l, m, n, d):
    nums = []
    for i in range(1, d + 1):
        nums.append(i)
    results = set()
    for num in nums:
        if num % k == 0:
            results.add(num)
        elif num % l == 0:
            results.add(num)
        elif num % m == 0:
            results.add(num)
        elif num % n == 0:
            results.add(num)
    return str(len(results))


def part4(n):
    result = 0
    if n % 2 == 0:
        result = int(n / 2)

    else:
        result = -1 * (int(n / 2) + 1)
    return str(result)


def part5(a):
    b = list(dict.fromkeys(a))
    max_index = 0
    i = 0
    maxi = a[0]
    while i < len(b):
        if b[i] >= maxi:
            maxi = b[i]
            max_index = i
        i += 1

    min_index = 0
    i = 0
    mini = max(b)
    while i < len(b):
        if b[i] <= mini:
            mini = b[i]
            min_index = i
        i += 1
    if len(a) == 2:
        first_out = str(len(a) - 1)

    else:
        first_out = str((max_index - 0) + ((len(b) - 1) - min_index))
    second_out = " ".join(str(x) for x in b)
    return first_out + "\n" + second_out


def part6(n):
    temp = 0
    first = 0
    second = 0
    if n % 2 == 0:
        temp = int(n / 2)
        first = temp
        second = n - temp
        while is_prime(first) or is_prime(second):
            first -= 1
            second += 1
            if first + second == n and (not is_prime(first) and not is_prime(second)):
                break

    else:
        temp = int(n / 2)
        first = temp
        second = n - first
        while is_prime(first) or is_prime(second):
            first -= 1
            second += 1
            if first + second == n and (not is_prime(first) and not is_prime(second)):
                break
    return f"{first} {second}"


def main(n):
    # Part 1 data: generate n numbers, increasing magnitude
    # ensure they are positive and vary
    n_values = [i * 11 + 1 for i in range(1, n + 1)]
    out1 = part1(n_values)

    # Part 2 data: permutation-like array of 1..n
    a2 = [(i * 2) % n + 1 for i in range(n)]  # values in [1,n]
    out2 = part2(n, a2)

    # Part 3 data: choose simple divisors and range
    k = 2 if n < 2 else 2
    l = 3 if n >= 3 else 1 + (n % 3)
    m = 4 if n >= 4 else 1 + (n % 4)
    p = 5 if n >= 5 else 1 + (n % 5)
    d = max(1, n * 5)
    out3 = part3(k, l, m, p, d)

    # Part 4 data: just n itself
    out4 = part4(n)

    # Part 5 data: array with duplicates, length n
    a5 = [(i // 2) % max(1, (n // 3 + 1)) for i in range(n)] if n > 0 else [0]
    out5 = part5(a5)

    # Part 6 data: use an even number >= 4 derived from n
    n6 = n * 2 + 4
    out6 = part6(n6)

    # print(out1)
    pass
    # print(out2)
    pass
    # print(out3)
    pass
    # print(out4)
    pass
    # print(out5)
    pass
    # print(out6)
    pass
if __name__ == "__main__":
    main(10)