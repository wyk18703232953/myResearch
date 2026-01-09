def main(n):
    # n: number of pairs, total elements = 2 * n
    size = 2 * n
    # Deterministic construction: two copies of sequence 0..n-1
    ar = [i for i in range(n)] + [i for i in range(n)]
    ans = 0
    for i in range(size):
        for j in range(i + 1, size):
            if ar[i] == ar[j]:
                while j != i + 1:
                    ar[j], ar[j - 1] = ar[j - 1], ar[j]
                    j -= 1
                    ans += 1
                break
    return ans


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    result = main(5)
    # print(result)
    pass