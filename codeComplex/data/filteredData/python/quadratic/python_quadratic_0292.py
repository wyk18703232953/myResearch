import random

def main(n: int) -> None:
    # 生成测试数据：n 对数字，每个数字出现两次，打乱顺序
    N = n
    pairs = list(range(1, N + 1)) * 2
    random.shuffle(pairs)

    visited = [False] * (N + 1)
    minimumSwaps = 0

    # 原逻辑：统计将相同数字配对所需的最小交换次数
    for i in range(2 * N):
        if not visited[pairs[i]]:
            visited[pairs[i]] = True
            count = 0
            for j in range(i + 1, 2 * N):
                if not visited[pairs[j]]:
                    count += 1
                elif pairs[i] == pairs[j]:
                    minimumSwaps += count

    print(minimumSwaps)


if __name__ == "__main__":
    # 示例：规模为 5，可按需修改或由外部调用 main(n)
    main(5)