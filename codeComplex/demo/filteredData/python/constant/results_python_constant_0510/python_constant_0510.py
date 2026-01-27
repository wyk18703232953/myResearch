def main(n):
    q = n
    results = []
    for i in range(q):
        x = i
        y = n - i
        k = n + i // 2 + 1

        if max(x, y) > k:
            results.append(-1)
        elif x == y and k == x + 1:
            results.append(k - 2)
            continue
        elif x % 2 == 1 and y % 2 == 1 and k % 2 == 0:
            results.append(k - 2)
            continue
        elif x % 2 == 0 and y % 2 == 0 and k % 2 == 1:
            results.append(k - 2)
            continue
        elif (x + y) % 2 == 0:
            results.append(k)

        else:
            results.append(k - 1)
    return results

if __name__ == "__main__":
    # example call for time complexity experiments
    res = main(10)
    for v in res:
        # print(v)
        pass