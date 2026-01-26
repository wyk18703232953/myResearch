def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def primeFactors(n):
    import math
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
        y = y >> 1
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


def core_logic(a, b):
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
        aa = []
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


def generate_inputs(n):
    if n < 1:
        n = 1
    if n > 18:
        n = 18
    a = ''.join(str((i * 7 + 3) % 10) for i in range(n))
    b_prefix_len = n // 2 + 1
    b_prefix = ''.join(str((i * 5 + 1) % 10) for i in range(b_prefix_len))
    if int(b_prefix[0]) == 0:
        b_prefix = '1' + b_prefix[1:]
    repeat_times = max(1, (n + b_prefix_len - 1) // b_prefix_len)
    b = (b_prefix * repeat_times)[:n]
    if int(b[0]) == 0:
        b = '1' + b[1:]
    return a, b


def main(n):
    a, b = generate_inputs(n)
    result = core_logic(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)