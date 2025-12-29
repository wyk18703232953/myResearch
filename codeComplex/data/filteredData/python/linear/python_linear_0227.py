import random

def main(n: int):
    # 根据规模 n 生成测试数据：长度为 n 的只含 '0' 和 '1' 的字符串
    s = ''.join(random.choice('01') for _ in range(n))

    # 原始逻辑
    result = '1' * min(s.count('1'), 1) + '0' * s.count('0')
    print(result)

if __name__ == "__main__":
    # 示例调用：可以按需修改 n 的大小
    main(10)