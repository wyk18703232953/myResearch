import random

def main(n: int):
    """
    n 为规模参数：
    - 当随机选择为模式 '1' 时：只生成并输出一行随机字符串
    - 当随机选择为模式 'else' 时：生成 n 个随机整数并按原逻辑处理
    """
    # 随机决定分支：'1' 分支或 else 分支
    first_input = random.choice(['1', '0'])

    if first_input == '1':
        # 模拟第二次 input()，生成长度在 [1, max(1,n)] 的随机字符串
        length = random.randint(1, max(1, n))
        s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
                    for _ in range(length))
        print(s)
    else:
        # 模拟整数序列输入：生成 n 个随机整数
        # 数值范围可按需要调整
        data = [random.randint(-10**6, 10**6) for _ in range(max(2, n))]
        x, *a, y = sorted(data)
        result = y - x + sum(abs(v) for v in a)
        print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)