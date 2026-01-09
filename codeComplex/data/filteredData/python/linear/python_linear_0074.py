def main(n):
    # Generate deterministic binary strings based on n
    # a_str length = n, b_str length = 2n (ensure b_len >= a_len and scalable)
    a = [i % 2 for i in range(n)]
    b = [(i * 2 + 1) % 2 for i in range(2 * n)]

    b_len = len(b)
    a_len = len(a)

    carCountPrefix = [[0 for _ in range(2)] for _ in range(b_len + 1)]
    b_zero_count = 0
    b_one_count = 0
    for b_i in range(b_len):
        if b[b_i] == 0:
            b_zero_count += 1
        elif b[b_i] == 1:
            b_one_count += 1
        carCountPrefix[b_i + 1][1] = b_one_count
        carCountPrefix[b_i + 1][0] = b_zero_count

    res = 0
    for cur in range(a_len):
        for dig in range(2):
            res += (carCountPrefix[b_len - a_len + cur + 1][dig] - carCountPrefix[cur][dig]) * abs(a[cur] - dig)

    # print(res)
    pass
if __name__ == "__main__":
    main(10)