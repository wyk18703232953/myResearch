import random

def main(n: int):
    # 生成长度为 n 的仅包含 '0' 和 '1' 的随机二进制串
    b = ''.join(random.choice('01') for _ in range(n))

    # 原逻辑：如果 b 为 '0' 或 '1'，直接输出 b
    if b == '0' or b == '1':
        print(b)
    else:
        # 统计 b 中 '0' 的个数
        s = len(list(filter(lambda x: x == '0', b)))
        # 输出 '1' 加上 s 个 '0'
        print('1' + '0' * s)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)