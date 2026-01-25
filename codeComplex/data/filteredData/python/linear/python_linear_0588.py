MOD = 1000000007

def solve_one(n, q, x, queries):
    sum_list = [0]
    for i, deliciousness in enumerate(x):
        sum_list.append(int(deliciousness) + sum_list[i])

    enjoyment_list = [0]
    for i in range(n):
        enjoyment_list.append((enjoyment_list[i] * 2 + 1) % MOD)

    outputs = []
    for l, r in queries:
        banhmi_count = r - l + 1
        delicious_count = sum_list[r] - sum_list[l - 1]
        non_delicious_count = banhmi_count - delicious_count
        enjoyment = 0
        if delicious_count == 0:
            enjoyment = 0
        else:
            enjoyment += enjoyment_list[delicious_count]
            enjoyment += (
                enjoyment_list[banhmi_count]
                - enjoyment_list[delicious_count]
                - enjoyment_list[non_delicious_count]
            )
            enjoyment %= MOD
        outputs.append(enjoyment)
    return outputs

def main(n):
    # n controls both string length and number of queries
    if n <= 0:
        return

    length = n
    q = n

    # Deterministically generate a binary string of length n
    # Pattern: x[i] = '1' if i % 3 == 0 or i % 5 == 0 else '0'
    x = ''.join('1' if (i % 3 == 0 or i % 5 == 0) else '0' for i in range(length))

    # Deterministically generate q queries [l, r] within [1, length]
    # For i in [0, q-1]:
    #   l = (i % length) + 1
    #   r = min(length, l + (i * 2) % max(1, length//2))
    queries = []
    half = max(1, length // 2)
    for i in range(q):
        l = (i % length) + 1
        span = (i * 2) % half
        r = l + span
        if r > length:
            r = length
        if l > r:
            l, r = r, l
        queries.append((l, r))

    outputs = solve_one(length, q, x, queries)
    for val in outputs:
        print(val)

if __name__ == "__main__":
    main(10)