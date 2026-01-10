def main(n):
    from collections import defaultdict

    # Deterministically generate k and list l based on n
    # Ensure k >= 1; avoid trivial all-1 or all-same patterns
    k = (n % 7) + 2  # k in [2,8]

    # Generate list l of length n with positive integers
    # Use a simple deterministic pattern involving k
    l = [(i * k + (i // 2) + 1) for i in range(1, n + 1)]

    if k == 1:
        print(n)
        return
    else:
        l.sort()
        ndict = defaultdict(list)
        for x in l:
            i_val = x
            while i_val % k == 0:
                i_val = i_val // k
            ndict[i_val].append(x)
        ans = 0
        for group in ndict.values():
            count = 0
            length = len(group)
            while count < length:
                if count == length - 1:
                    ans += 1
                    break
                if group[count] * k != group[count + 1]:
                    ans += 1
                    count += 1
                else:
                    ans += 1
                    count += 2
        print(ans)


if __name__ == "__main__":
    main(1000)