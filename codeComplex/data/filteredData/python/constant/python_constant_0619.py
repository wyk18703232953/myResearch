def main(n):
    # Interpret n as the number of test cases
    t = n
    results = []
    for i in range(t):
        # Deterministic generation of l, r based on i
        # Ensure l <= r and both grow with n for scalability
        l = i + 1
        r = (i + 1) * 3
        if (l - r) % 2 == 1:
            if l % 2:
                results.append((r - l + 1) // 2)

            else:
                results.append(-((r - l + 1) // 2))

        else:
            ans = 0
            if l % 2:
                ans = ans + (r - l) // 2

            else:
                ans = ans - (r - l) // 2
            if r % 2:
                ans = ans - r

            else:
                ans = ans + r
            results.append(ans)
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)