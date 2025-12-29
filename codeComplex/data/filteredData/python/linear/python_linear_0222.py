import random

def main(n: int):
    # 根据 n 生成测试数据：长度为 n 的仅由 '0' 和 '1' 组成的字符串
    s = ''.join(random.choice('01') for _ in range(n))

    if n == 1:
        print(s)
    else:
        zeros = s.count('0')
        print('1' + zeros * '0')


if __name__ == "__main__":
    # 示例：可自行修改 n 测试规模
    main(5)