import random

def main(n):
    # 生成测试数据：n 行，每行一对 (a, b)
    # 这里随机构造 a, b，确保 a >= b >= 0
    # 你可以根据需要修改数据生成策略
    pairs = []
    for _ in range(n):
        a = random.randint(0, 10**6)
        b = random.randint(0, a)  # 保证 b <= a，防止出现负数太多
        pairs.append((a, b))

    # 原逻辑开始
    length = n
    start = []
    end = []
    for i in range(length):
        a, b = pairs[i]
        e, s = a - b, a + b
        end.append([e, i])
        start.append([s, i])

    end.sort(key=lambda x: x[0])
    start.sort(key=lambda x: x[0])

    cant_visit = set()
    answer = 0
    end_index = 0
    for s, i in start:
        if i not in cant_visit:
            answer += 1
            while end_index < length and end[end_index][0] < s:
                cant_visit |= {end[end_index][1]}
                end_index += 1

    print(answer)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)