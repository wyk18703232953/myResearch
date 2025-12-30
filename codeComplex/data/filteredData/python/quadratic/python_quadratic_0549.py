import random

def main(n: int) -> str:
    # 随机生成 e，保证 (n - e) 为非负偶数
    # 原代码中只要求 n,e 来自输入，这里用简单规则生成测试数据
    if n <= 0:
        return ""

    # 任选一个 d ∈ [0, n//2]，并由 d 反推 e
    d = random.randint(0, n // 2)
    e = n - 2 * d  # 确保 (n - e) // 2 == d 且 e >= 0

    # 以下为原逻辑，只是去掉 input()，并封装为函数
    nn = n  # 使用局部变量避免修改参数
    d_local = (nn - e) // 2
    q = []

    while nn > 0:
        i = min(nn, d_local)
        while i > 0:
            q.append('1')
            i -= 1
            nn -= 1
        if nn > 0:
            q.append('0')
            nn -= 1

    return "".join(q)


if __name__ == "__main__":
    # 示例：规模为 10 时运行
    result = main(10)
    print(result)