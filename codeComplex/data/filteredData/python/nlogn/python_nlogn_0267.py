import random

def main(n: int):
    # 生成测试数据：n 个线段 [a, b]，保证 a <= b
    segments = []
    for i in range(n):
        a = random.randint(0, 100)
        b = random.randint(a, a + 100)
        segments.append(((a, b), i + 1))  # ( (a,b), 原始下标从1开始 )

    # 按照原程序逻辑排序
    segments.sort(key=lambda x: (x[0][0], -x[0][1]))

    last_r = 0
    last_index = 0

    for segment, index in segments:
        if last_r >= segment[1]:
            print(index, last_index)
            break

        last_r = segment[1]
        last_index = index
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：运行规模为 n=10 的测试
    main(10)