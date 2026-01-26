def prime(n):
    j = 3
    while j * j <= n:
        if n % j == 0:
            return False
        j += 2
    return True

# Precompute ref and arr exactly as in the original code
ref = [2]
for j in range(3, 1000, 2):
    if prime(j):
        ref.append(j)

def check(n):
    for j in range(1, len(ref) - 1):
        v = n - ref[j] - 1
        if ref[j - 1] == v or ref[j + 1] == v:
            return True
        if j > n:
            break
    return False

arr = []
for j in range(3, 1001, 2):
    if prime(j) and check(j):
        arr.append(j)

def main(n):
    # 映射规则：
    # n 为输入规模，生成一组确定性的 (N, K)
    # N = min(n, 1000) 保证不超过原算法预处理范围
    # K = (n // 2) + 1，用于控制判定阈值
    N = n if n > 0 else 1
    if N > 1000:
        N = 1000
    K = (n // 2) + 1 if n > 0 else 1

    count = 0
    for j in range(2, N + 1):
        if j in arr:
            count += 1
    if count >= K:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：以不同规模 n 调用 main
    main(10)