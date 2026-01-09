def solve(a_str, b_str):
    a = list(map(int, a_str.strip()))
    b = list(map(int, b_str.strip()))
    dff = len(b) - len(a)
    if dff < 0:
        return 0
    lb = len(b)
    c = [0] * (lb + 1)
    for i in range(lb):
        c[i + 1] = c[i] + b[i]
    ans = 0
    for i in range(len(a)):
        item = a[i]
        seg_sum = c[dff + i + 1] - c[i]
        if item:
            ans += (dff + 1 - seg_sum)

        else:
            ans += seg_sum
    return ans


def main(n):
    """
    n: 控制测试数据规模（长度）
    这里简单生成：
    - a 为长度 n 的二进制串
    - b 为长度 n 或 n+1 的二进制串（保证与原逻辑兼容）
    """
    if n <= 0:
        return 0

    # 简单的可重复生成方式：使用循环模式
    a_str = ''.join('01'[(i // 1) % 2] for i in range(n))
    # 保证 b 的长度 >= a 的长度一半左右，且有变化
    m = n + (n // 2) + 1
    b_str = ''.join('10'[(i // 1) % 2] for i in range(m))

    return solve(a_str, b_str)


if __name__ == "__main__":
    # 示例：规模为 5
    # print(main(5))
    pass