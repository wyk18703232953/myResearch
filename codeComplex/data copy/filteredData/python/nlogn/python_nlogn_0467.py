def main(n):
    # Generate deterministic data based on n
    if n <= 0:
        return
    k = max(1, n // 2)
    a = [(i * 3 + 1) % (2 * n + 1) for i in range(n)]

    if n == 1:
        # print(a[0])
        pass
        # print(1)
        pass

    else:
        lst = sorted(a)[-k:]
        total = sum(lst)
        # print(total)
        pass
        ln = len(lst)
        positions = [0]
        cnt = 0
        for i in range(n):
            if cnt == k - 1:
                break
            for j in range(ln):
                if a[i] == lst[j]:
                    lst[j] = -1
                    positions.append(i + 1)
                    cnt += 1
                    break
        ln = len(positions)
        for i in range(1, ln):
            # print(positions[i] - positions[i - 1], end=" ")
            pass
        # print(n - positions[-1])
        pass
if __name__ == "__main__":
    main(10)