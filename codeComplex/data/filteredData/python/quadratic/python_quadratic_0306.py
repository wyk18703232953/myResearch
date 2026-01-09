def main(n):
    # Interpret n as the length of the list; choose k deterministically
    if n <= 0:
        return 0.0
    k = max(1, n // 3)
    l = [(i * 7 + 3) % 1000 for i in range(n)]

    ans = 0.0
    for i in range(n):
        avg, count = 0.0, 0
        for j in range(i, n):
            count += l[j]
            if j - i + 1 >= k:
                avg = count / (j - i + 1)
            if avg > ans:
                ans = avg
    return ans


if __name__ == "__main__":
    # Example call for time complexity experiment
    result = main(1000)
    # print(result)
    pass