def main(n):
    if n <= 0:
        return 0

    a = list(range(1, n + 1))

    a = sorted(list(set(a)))
    n = len(a)
    used = [0] * n
    cnt = 0
    for i in range(n):
        if not used[i]:
            used[i] = 1
            cnt += 1
            for j in range(i + 1, n):
                if a[j] % a[i] == 0:
                    used[j] = 1
    return cnt


if __name__ == "__main__":
    # print(main(10))
    pass