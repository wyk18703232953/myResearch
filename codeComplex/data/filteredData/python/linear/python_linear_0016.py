def f(n):
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True

def solve(n, k):
    a = []
    x = 0
    for i in range(2, n + 1):
        if f(i):
            a.append(i)
    for i in range(len(a) - 2):
        if a[i] + a[i + 1] + 1 in a:
            x += 1
    if x >= k:
        return "YES"
    else:
        return "NO"

def main(n):
    # 将输入规模 n 映射为原程序中的 (n, k)
    # 这里设定:
    #   原 n := n
    #   原 k := max(1, n // 10)
    original_n = n
    original_k = max(1, n // 10)
    result = solve(original_n, original_k)
    print(result)

if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 进行规模实验
    main(100)