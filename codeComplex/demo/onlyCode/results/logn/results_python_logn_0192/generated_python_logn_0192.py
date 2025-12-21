def find_bin_value(num, s):
    i = 9 * num * 11
    for _ in range(100):
        add = 0
        a = str(i)
        for k in range(10):
            add += a.count(str(k)) * k
        if i - add >= s:
            return i
        i += 1
    return -1

def main(n):
    s = n
    i = 0
    j = 10**30
    while i < j:
        m = (i + j) // 2
        if find_bin_value(m, s) == -1:
            i = m + 1
        else:
            j = m
    return max(0, n - find_bin_value(i, s) + 1)

if __name__ == "__main__":
    print(main(1000))