import random

def main(n: int):
    # 根据规模 n 生成测试数据字符串 s
    # 这里约定：长度为 n，由 '0' 和 '1' 随机组成，且至少有一个 '1'，避免总为 "0"
    if n <= 0:
        s = "0"
    else:
        s = ''.join(random.choice('01') for _ in range(n))
        if set(s) == {'0'}:
            # 若全为 0，则随机挑一个位置改为 1，保证不全为 0
            idx = random.randrange(n)
            s = s[:idx] + '1' + s[idx + 1:]

    # 原逻辑
    if s == '0':
        print(0)
    else:
        print("1" + "0" * s.count('0'))


if __name__ == "__main__":
    # 示例：调用 main，n 为测试数据规模
    main(10)