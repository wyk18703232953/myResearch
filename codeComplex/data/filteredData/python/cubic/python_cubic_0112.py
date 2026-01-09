def get_gdict(arr):
    gdict = dict()
    for i in range(len(arr)):
        if arr[i] in gdict:
            gdict[arr[i]] += 1

        else:
            gdict[arr[i]] = 1
    return gdict


def initial_check(barr, garr):
    for i in garr:
        if i < barr[-1]:
            return False
    return True


def core_logic(n, m, barr, garr):
    barr.sort()
    garr.sort()
    ans = 0
    gdict = get_gdict(garr)
    if initial_check(barr, garr):
        count = m
        b = n - 1
        g = m - 1
        while count > 0 and b >= 0:
            tempb = [barr[b]] * m
            for i in range(len(tempb)):
                if count <= 0:
                    for j in range(i, m):
                        ans += tempb[i]
                    break

                if tempb[i] in gdict:
                    gdict[tempb[i]] -= 1
                    ans += tempb[i]
                    count -= 1
                    if gdict[tempb[i]] == 0:
                        del gdict[tempb[i]]

                else:
                    if i == 0:
                        ans += tempb[i]
                        continue
                    for k in range(g, -1, -1):
                        if garr[k] in gdict:
                            ans += garr[g]
                            g = k - 1
                            count -= 1
                            break
            b -= 1

        while b >= 0:
            ans += m * barr[b]
            b -= 1
        return ans

    else:
        return -1


def generate_data(n):
    if n < 2:
        n = 2
    m = n
    barr = [i + 1 for i in range(n)]
    garr = [i + 1 for i in range(m)]
    return n, m, barr, garr


def main(n):
    n_val, m_val, barr, garr = generate_data(n)
    result = core_logic(n_val, m_val, barr, garr)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)