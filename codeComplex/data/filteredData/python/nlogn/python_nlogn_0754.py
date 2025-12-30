import random

def main(n: int):
    """
    n: 规模参数，表示测试组数 t。
       每组内数组长度和数值根据 n 自动生成。
    """
    t = n
    results = []

    for _ in range(t):
        # 为每一组生成数组长度：1 到 max(2, n) 之间
        length = random.randint(2, max(2, n))
        # 生成数组元素：1 到 2n 之间
        arr = [random.randint(1, 2 * n) for _ in range(length)]

        arr.sort(reverse=True)
        # 原逻辑：min(arr[1] - 1, len(arr) - 2)
        ans = min(arr[1] - 1, len(arr) - 2)
        results.append(ans)

    # 输出所有结果
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)