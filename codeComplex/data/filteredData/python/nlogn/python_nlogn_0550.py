def main(n):
    if n <= 0:
        return ""
    # 确定性生成数组：1..n 的一个固定排列（这里使用简单的“向右循环移位一位”）
    arr = list(range(2, n + 1)) + [1]

    pos = {}
    for i in range(n):
        pos[arr[i]] = i

    if n == 1:
        ans_str = "B"

    else:
        ans = ["Q"] * n
        ans[pos[1]] = "A"
        ans[pos[n]] = "B"
        for i in range(n - 1, 0, -1):
            flag = 0
            p = pos[i]
            j = 1
            while p + j * i < n:
                if ans[p + j * i] == "B":
                    flag = 1
                    ans[pos[i]] = "A"
                    break
                j += 1
            if flag == 0:
                j = 1
                while p - j * i >= 0:
                    if ans[p - j * i] == "B":
                        flag = 1
                        ans[pos[i]] = "A"
                        break
                    j += 1
            if flag == 0:
                ans[pos[i]] = "B"
        ans_str = "".join(ans)

    # print(ans_str)
    pass
    return ans_str


if __name__ == "__main__":
    main(10)