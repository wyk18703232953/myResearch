import random

def main(n):
    # 生成规模为 n 的测试数据：n 个线段 (l, r)
    # 这里简单生成：l 递增，r 为 l 之后的随机值，保证大部分情况下不存在“坏”情况
    segments = []
    current_l = 0
    for _ in range(n):
        length = random.randint(1, 10)
        l = current_l
        r = l + length
        segments.append((l, r))
        current_l += random.randint(0, 5)

    # 按原代码逻辑：对 (l, r, idx) 排序并检测条件
    segments = sorted((L, R, idx + 1) for idx, (L, R) in enumerate(segments))

    prev = (-1, -1, -1)
    for segment in segments:
        # 保持原代码的断言逻辑
        assert prev[0] <= segment[0]
        if prev[0] == segment[0]:
            assert prev[1] <= segment[1]
            print(prev[2], segment[2])
            break
        elif prev[1] >= segment[1]:
            print(segment[2], prev[2])
            break
        prev = segment
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)