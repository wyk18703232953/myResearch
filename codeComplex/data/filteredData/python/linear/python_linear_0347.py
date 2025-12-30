import random

def main(n):
    # 依据 n 构造 m（例如构造一条链式图：m = max(n-1, 0)）
    if n <= 0:
        print("")
        return

    m = max(n - 1, 0)

    # 生成测试数据：m 条边，简单构造为一条链 1-2-3-...-n
    edges = []
    for i in range(1, n):
        edges.append((i, i + 1))

    # 原逻辑：只使用 n, m 与边的输入，但边在原程序中并未参与计算
    # 这里只是保持同样的结构
    ans = [0] * n
    for i in range(1, n, 2):
        ans[i] = 1

    print(''.join(map(str, ans)))

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)