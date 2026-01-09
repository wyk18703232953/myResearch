def main(n):
    # Interpret n as the length of array a
    # Deterministically generate c and a
    if n <= 0:
        # print(0)
        pass
        return

    # Set c deterministically based on n, within the allowed value range
    max_val = 500000
    c = (n % max_val) + 1  # ensure 1..500000

    # Generate a deterministically: values in [1, max_val], with some occurrences of c
    a = []
    for i in range(n):
        # Create a pattern with periodic c and other values
        if i % 5 == 0:
            val = c

        else:
            # some other value different from c
            val = ((i * 7) % max_val) + 1
            if val == c:
                val = (val % max_val) + 1
        a.append(val)

    nums = [[0] for _ in range(500001)]
    freq = [0] * 500001
    minus = 0

    for i in a:
        if i == c:
            minus += 1

        else:
            freq[i] += 1
            nums[i].append(freq[i] - minus)

    tot = minus
    suff = [i[:] for i in nums]

    for i in range(500001):
        for j in range(len(nums[i]) - 2, 0, -1):
            suff[i][j] = max(suff[i][j], suff[i][j + 1])

    freq = [0] * 500001
    ans = tot

    for i in a:
        if i == c:
            continue
        freq[i] += 1
        ans = max(ans, suff[i][freq[i]] - nums[i][freq[i]] + 1 + tot)

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)