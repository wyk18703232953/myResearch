import random

def main(n: int):
    # 根据 n 生成测试数据，这里直接使用 n 作为原程序中的输入
    # 若需更复杂数据，可在此处扩展生成逻辑
    ans = 0
    for i in range(2, n + 1):
        for j in range(i + i, n + 1, i):
            ans += 4 * j // i
    print(ans)


if __name__ == "__main__":
    # 示例：使用规模 n = 100 运行
    main(100)