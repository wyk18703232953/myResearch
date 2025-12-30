import random

def main(n: int):
    # 生成测试数据：长度为 n 的字符串，由 'H' 和 'T' 随机组成
    s = ''.join(random.choice('HT') for _ in range(n)) * 2

    h = s.count('H') // 2
    ans = h - max(s[i:i + h].count('H') for i in range(n))
    print(ans)


if __name__ == "__main__":
    # 示例：可自行修改 n 测试不同规模
    main(10)