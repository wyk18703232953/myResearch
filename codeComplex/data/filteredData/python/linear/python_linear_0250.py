import random

def main(n):
    # 随机生成 k，范围 [0, (n-2)*2]，避免明显无解情况
    max_k = max(0, (n - 2) * 2)
    k = random.randint(0, max_k)

    s = [["."] * n for _ in range(4)]
    orig_k = k  # 仅用于调试需要时查看原始 k，可删除

    if k % 2 == 0:
        for j in range(1, n - 1):
            if k == 0:
                break
            s[1][j] = "#"
            s[2][j] = "#"
            k -= 2
    else:
        cen = n // 2
        s[1][cen] = "#"
        k -= 1
        for i in range(1, 3):
            for j in range(1, cen):
                if k > 0:
                    k -= 2
                    s[i][j] = s[i][-j - 1] = "#"

    if k == 0:
        print("YES")
        for i in range(4):
            print("".join(s[i]))
    else:
        print("NO")

if __name__ == "__main__":
    # 示例：调用 main(7)
    main(7)