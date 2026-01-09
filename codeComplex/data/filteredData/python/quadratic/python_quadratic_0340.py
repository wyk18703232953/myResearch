import string

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def main(n):
    if n <= 0:
        return

    # 确定性生成字符串 a 和 b，长度均为 n
    letters = string.ascii_lowercase
    L = len(letters)
    a = [letters[i % L] for i in range(n)]
    # 生成 b 为 a 的一个确定性排列（例如整体右移一位，循环）
    if n > 1:
        b = [a[-1]] + a[:-1]

    else:
        b = a[:]

    res_a = dict().fromkeys(list(string.ascii_lowercase), 0)
    res_b = dict().fromkeys(list(string.ascii_lowercase), 0)

    for ch in a:
        res_a[ch] += 1
    for ch in b:
        res_b[ch] += 1

    can = True
    for ch in res_a:
        if res_a[ch] != res_b[ch]:
            can = False
            break

    if not can:
        # print(-1)
        pass

    else:
        ans = []
        for i in range(n):
            if a[i] == b[i]:
                continue

            else:
                idx = -1
                for j in range(i + 1, n):
                    if a[j] == b[i]:
                        idx = j
                        break
                for j in range(idx, i, -1):
                    ans.append(j)
                    swap(a, j, j - 1)
        # print(len(ans))
        pass

        if ans:
            # print(' '.join(map(str, ans)))
            pass

        else:
            # print()
            pass
if __name__ == "__main__":
    main(10)