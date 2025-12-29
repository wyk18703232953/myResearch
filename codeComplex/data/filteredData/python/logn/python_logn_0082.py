import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里假设 n 控制数字的比特长度，即 l, r < 2**n
    # 并保证 l <= r
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    diff = r ^ l
    result = (1 << diff.bit_length()) - 1
    print(result)


if __name__ == "__main__":
    # 示例：规模为 10，可自行修改
    main(10)