from __future__ import division


def main(n):
    """
    n: 规模参数，正整数
    程序逻辑：根据 n 和生成的 s，计算 ceil(s / n)
    这里根据 n 生成测试数据：设 s = n * n + n // 2
    """
    # 生成测试数据
    s = n * n + n // 2

    # 原逻辑：输出 ceil(s / n)
    if s % n == 0:
        result = s // n
    else:
        result = s // n + 1

    # 直接返回结果，而不是使用 stdout
    return result


if __name__ == "__main__":
    # 示例：可以自行修改 n 测试
    print(main(10))