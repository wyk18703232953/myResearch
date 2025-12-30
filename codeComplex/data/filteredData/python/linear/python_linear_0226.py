import random

def main(n: int):
    # 生成长度为 n 的随机二进制字符串作为测试数据
    # 确保至少有一个 '1'，否则原逻辑会输出 '0'
    if n <= 0:
        binary_number = '0'
    else:
        # 随机生成，并保证不全是 '0'
        while True:
            binary_number = ''.join(random.choice('01') for _ in range(n))
            if '1' in binary_number:
                break

    # 原逻辑开始
    if binary_number == '0':
        print('0')
    else:
        count_0 = sum(1 for b in binary_number if b == '0')
        count_1 = sum(1 for b in binary_number if b == '1')
        print('1' + '0' * count_0)

if __name__ == "__main__":
    # 示例调用：n 为规模参数，可自行修改
    main(10)