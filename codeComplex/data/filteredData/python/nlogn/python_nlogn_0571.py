import random

def main(n: int):
    # 生成测试数据 a[1..n]，满足原程序逻辑要求：
    # 对于 i >= 2，有 a[i] 在 [1, i-1] 中（类似构造一棵有根树的父节点数组）
    a = [0, 0]  # 预留 a[0], a[1]
    for i in range(2, n + 1):
        a.append(random.randint(1, i - 1))

    ans = [0] * (n + 1)
    for i in range(n, 1, -1):
        if ans[i] == 0:
            ans[i] = 1
        ans[a[i]] += ans[i]
    if n == 1:
        ans[1] = 1
    ans = ans[1:]
    ans.sort()
    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需修改 n
    main(10)