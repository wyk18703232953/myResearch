def main(n):
    pw = [1, 4]
    for i in range(2, 32):
        pw.append(pw[i - 1] * 4)
    t = n
    results = []
    for cas in range(t):
        k = cas + 1
        nn = n + cas
        last = 1
        path = 1
        ans = nn
        i = 0
        while True:
            if (pw[i + 1] - 1) // 3 > k:
                ans -= i
                last = k - (pw[i] - 1) // 3
                break
            i = i + 1
            path *= 2
        sp = path * 2 - 1
        if (ans < 0) or ((ans == 0) and (last > 0)):
            results.append(("No",))
            continue
        sq = path * path - sp
        if (ans == 1) and (last > sq) and (last < sp):
            results.append(("No",))
            continue
        elif (ans == 1) and (last >= sp):
            ans = ans - 1
        results.append(("Yes", ans))
    return results

if __name__ == "__main__":
    print(main(5))