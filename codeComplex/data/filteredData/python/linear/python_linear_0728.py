import os

def log(*args, **kwargs):
    if os.environ.get('CODEFR'):
        print(*args, **kwargs)


def main(n):
    # 生成测试数据：k 为 0 到 n 之间的某个值
    # 这里选择一个简单规则：k = n // 2
    k = n // 2

    # 原逻辑
    s = '0' * ((n - k) // 2) + '1'

    output = []
    for i in range(n):
        output.append(s[i % len(s)])
    print(''.join(output))


if __name__ == "__main__":
    # 示例：可修改此处以测试不同规模
    main(10)