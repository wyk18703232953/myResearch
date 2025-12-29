import random

def main(n: int):
    # 生成测试数据：长度为 n，由 'H' 和 'T' 随机组成
    s = ''.join(random.choice('HT') for _ in range(n))

    # 原逻辑开始
    s2 = s * 2
    h = s2.count('H') // 2
    ans = h - max(s2[i:i + h].count('H') for i in range(n))

    # 输出结果（可根据需要改为 return ans）
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)