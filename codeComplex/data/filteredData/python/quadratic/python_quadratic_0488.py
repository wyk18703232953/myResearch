def main(n):
    # Deterministic generation of le and ri based on n
    # Here we choose le and ri such that a valid 'check' exists and is simple:
    # Let check[i] = i (strictly increasing), so:
    #   le[i] = number of j < i with check[j] > check[i] = 0
    #   ri[i] = number of j > i with check[j] > check[i] = 0
    # Then original relation: check[i] = n - le[i] - ri[i] => le[i] + ri[i] = n - check[i]
    # We can make le[i] = 0 and ri[i] = n - i
    # But that gives le[i] + ri[i] = n - i != n - check[i] (since check[i] = i)
    # To respect original construction check[i] = n - le[i] - ri[i],
    # we directly construct le and ri from a chosen check.
    check = [i for i in range(n)]
    le = [0] * n
    ri = [0] * n
    # Compute le and ri from check so that the later consistency checks pass
    for i in range(n):
        cnt_left = 0
        for j in range(i - 1, -1, -1):
            if check[j] > check[i]:
                cnt_left += 1
        le[i] = cnt_left
        cnt_right = 0
        for j in range(i + 1, n):
            if check[j] > check[i]:
                cnt_right += 1
        ri[i] = cnt_right
    # Now override check exactly as in original program using le and ri
    notp = False
    check2 = []
    for i in range(n):
        check2.append(n - le[i] - ri[i])
    for i in range(n):
        tot = 0
        for j in range(i - 1, -1, -1):
            if check2[j] > check2[i]:
                tot += 1
        if tot != le[i]:
            notp = True
            break
    if not notp:
        for i in range(n):
            tot = 0
            for j in range(i + 1, n):
                if check2[j] > check2[i]:
                    tot += 1
            if tot != ri[i]:
                notp = True
                break
    if notp:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        # print(*check2)
        pass
if __name__ == "__main__":
    main(10)