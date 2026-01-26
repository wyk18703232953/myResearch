def main(n):
    # Generate deterministic inputs a and b based on n
    # a: n-digit number with pattern (i % 10)
    # b: n-digit number with pattern ((i + 3) % 10), but ensure int(a) <= int(b) when lengths equal
    if n <= 0:
        return

    # Construct string a
    a = ''.join(str(i % 10) for i in range(n))

    # Construct preliminary b
    b_digits = [(i + 3) % 10 for i in range(n)]
    b = ''.join(str(d) for d in b_digits)

    # Ensure when lengths equal, int(a) <= int(b) to avoid trivial "len(a) < len(b)" branch dominating
    # If not, adjust b deterministically by increasing the first digit that is smaller than 9
    if len(a) == len(b) and int(a) > int(b):
        b_list = [int(ch) for ch in b]
        for i in range(len(b_list) - 1, -1, -1):
            if b_list[i] < 9:
                b_list[i] += 1
                break
        b = ''.join(str(d) for d in b_list)

    la = [int(x) for x in a]
    res = []
    la.sort()
    la = la[::-1]
    lb = [int(x) for x in b]
    cnt = [0] * 20

    def check():
        tres = 0
        for x in range(len(res)):
            tres *= 10
            tres += int(res[x])
        return tres <= int(b)

    if len(a) < len(b):
        for i in range(len(la)):
            # print(la[i], end='')
            pass
        # print()
        pass

    else:
        for i in range(len(la)):
            cnt[la[i]] += 1
        flag = 0
        for i in range(len(lb)):
            if flag == 0 and cnt[lb[i]]:
                res.append(lb[i])
                cnt[lb[i]] -= 1

            else:
                flag = i - 1
                for j in range(lb[i] - 1, -1, -1):
                    if cnt[j]:
                        res.append(j)
                        cnt[j] -= 1
                        break
                for j in range(9, -1, -1):
                    while cnt[j]:
                        res.append(j)
                        cnt[j] -= 1
                break
        while not check():
            temp = []
            cnt = [0] * 20
            for x in range(flag):
                temp.append(res[x])
                cnt[res[x]] -= 1
            for i in la:
                cnt[i] += 1
            res = temp
            for v in range(lb[flag] - 1, -1, -1):
                if cnt[v]:
                    res.append(v)
                    cnt[v] -= 1
                    break
            for v in range(9, -1, -1):
                while cnt[v]:
                    res.append(v)
                    cnt[v] -= 1
            flag -= 1
        for i in range(len(res)):
            # print(res[i], end='')
            pass
        # print()
        pass
if __name__ == "__main__":
    # Example call for experimentation; adjust n as needed
    main(10)