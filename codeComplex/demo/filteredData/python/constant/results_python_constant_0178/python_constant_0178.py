from math import gcd

def func(left: int, right: int):
    if left == 1:
        left += 1
    if right - left < 2:
        return -1

    if left & 1:
        if right - left > 2:
            left += 1
            return '{} {} {}'.format(left, left + 1, left + 2)

        else:
            if gcd(left, left + 2) != 1:
                return '{} {} {}'.format(left, left + 1, left + 2)
            return -1
    return '{} {} {}'.format(left, left + 1, left + 2)


def main(n):
    # 对于这个程序，原始输入是两个整数 left, right
    # 将 n 解释为区间长度，使得 right - left + 1 = n
    # 选择一个确定性的映射：left = 1，right = n
    # 当 n < 3 时，算法会立即返回 -1，这也符合原逻辑
    left = 1
    right = n
    result = func(left, right)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模化实验
    main(10)