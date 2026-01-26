n_global = None

def build_input_from_n(n):
    # 原程序输入结构：单行两个整数 n, k
    # 这里将 n 视为规模，映射到 (N, K)
    # 设定 N = max(3, n)，保证有意义的网格
    N = max(3, n)
    # K 最大不超过 (N-2)*2，因为两行每行有 N-2 个可放置的位置
    max_k = (N - 2) * 2
    if max_k < 0:
        max_k = 0
    # 让 K 在 [0, max_k] 内随 n 确定性变化
    if max_k == 0:
        K = 0

    else:
        K = n % (max_k + 1)
    return N, K

def core_logic(N, K):
    n = N
    k = K
    s=[["."]*n for _ in range(4)]
    if k%2==0:
        for j in range(1,n-1):
            if k==0:
                break
            s[1][j]="#"
            s[2][j]="#"
            k-=2

    else:
        cen=n//2
        s[1][cen]="#"
        k-=1
        for i in range(1,3):
            for j in range(1,cen):
                if k>0:
                    k-=2
                    s[i][j]=s[i][-j-1]="#"
    outputs = []
    if k==0:
        outputs.append("YES")
        for i in range(4):
            outputs.append("".join(s[i]))

    else:
        outputs.append("NO")
    return "\n".join(outputs)

def main(n):
    N, K = build_input_from_n(n)
    result = core_logic(N, K)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)