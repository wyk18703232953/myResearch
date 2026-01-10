def main(n):
    from collections import Counter

    # Deterministic data generation
    # Map n to original n and k, and generate li of length n
    if n <= 0:
        return 0

    orig_n = n
    k = n // 2 + 1  # deterministic k depending on n
    li = [(i * 2) % (n + 3) for i in range(orig_n)]  # deterministic list

    dic = Counter(li)
    li = list(set(li))
    li.sort()
    n_unique = len(li)

    for i in range(1, n_unique):
        for j in range(i - 1, -1, -1):
            if li[j] + k >= li[i] and dic[li[j]] != 0:
                dic[li[j]] = 0
            else:
                break

    result = sum(dic.values())
    return result


if __name__ == "__main__":
    # Example deterministic call
    print(main(10))