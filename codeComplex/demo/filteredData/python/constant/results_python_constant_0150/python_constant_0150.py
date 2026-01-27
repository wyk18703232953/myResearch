def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def logic_block1(x):
    digits = []
    new_digits = set()
    outputs = []
    n = x
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
    return outputs


def logic_block2(n):
    a = list(range(1, n + 1))
    b = list(range(1, n + 1))
    results = []
    for l in b:
        results.append(a.index(l) + 1)
    return [" ".join(str(r) for r in results)]


def logic_block3(k, l, m, n, d):
    nums = list(range(1, d + 1))
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
    return [str(len(results))]


def logic_block4(n):
    if n % 2 == 0:
        result = int(n / 2)
    else:
        result = -1 * (int(n / 2) + 1)
    return [str(result)]


def logic_block5(arr):
    a = arr
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
        res1 = len(a) - 1
    else:
        res1 = (max_index - 0) + ((len(b) - 1) - min_index)
    return [str(res1), " ".join(str(x) for x in b)]


def logic_block6(n):
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
    return [f"{first} {second}"]


def main(n):
    outputs = []

    # Block 1: use n as count and as value generator
    for i in range(1, n + 1):
        x = i * 11
        outputs.extend(logic_block1(x))

    # Block 2: permutation index finding on size n
    outputs.extend(logic_block2(n))

    # Block 3: divisibility counting, scale d with n
    k = 2 if n < 2 else 2
    l = 3 if n < 3 else 3
    m = 4 if n < 4 else 4
    p = 5 if n < 5 else 5
    d = max(1, n * 10)
    outputs.extend(logic_block3(k, l, m, p, d))

    # Block 4: even/odd function on n
    outputs.extend(logic_block4(n))

    # Block 5: arrival logic on an array of size n
    arr = [((i * 3) % (n + 5)) + 1 for i in range(n if n > 0 else 1)]
    outputs.extend(logic_block5(arr))

    # Block 6: prime-split-like logic on 2*n (ensuring even > 2 for n>1)
    val = max(4, 2 * n)
    outputs.extend(logic_block6(val))

    for line in outputs:
        print(line)


if __name__ == "__main__":
    main(5)