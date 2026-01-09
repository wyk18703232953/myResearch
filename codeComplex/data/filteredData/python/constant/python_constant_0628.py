def main(n):
    q = n
    results = []
    for i in range(q):
        l = 2 * i + 1
        r = l + 2 * (i + 1)
        sign = -1 if l % 2 else 1
        if (r - l) % 2:
            results.append(-sign * (r - l + 1) // 2)

        else:
            results.append(sign * (l + (r - l) // 2))
    return results

if __name__ == "__main__":
    res = main(10)
    for x in res:
        # print(x)
        pass