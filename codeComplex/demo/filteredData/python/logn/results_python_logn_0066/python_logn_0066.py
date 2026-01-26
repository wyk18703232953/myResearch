def main(n):
    """
    规模参数 n 用于生成两个测试整数 a 和 b：
    这里示例为：
        a = 2**(n//2) + 3
        b = 2**(n//2 + 1) + 5
    然后运行原逻辑，返回计算结果 ans。
    """

    # 原程序中的全局变量改为局部
    arra = []
    arrb = []
    temp = 1
    ans = 0

    # 使用闭包形式的 fill 和 check，避免使用全局 n、arra、arrb
    def fill(target_list, cnt):
        # 在列表头部补 cnt 个 0
        for _ in range(cnt):
            target_list.insert(0, 0)

    def check():
        # 检查 arra 与 arrb 首位是否相同
        for i, j in zip(arra, arrb):
            if i == j:
                return 1

            else:
                return 0

    def Engine1(num):
        if num > 1:
            Engine1(num // 2)
        arra.append(num % 2)

    def Engine2(num):
        if num > 1:
            Engine2(num // 2)
        arrb.append(num % 2)

    # ---------- 根据 n 生成测试数据（可按需要自行修改策略） ----------
    # 保证生成的数较大一些但不溢出：2^(n//2+1) 级别
    if n < 1:
        a, b = 1, 1

    else:
        a = (1 << (n // 2)) + 3
        b = (1 << (n // 2 + 1)) + 5
    # -------------------------------------------------------------

    # 原逻辑开始
    Engine1(a)
    Engine2(b)

    diff = abs(len(arra) - len(arrb))
    if len(arra) > len(arrb):
        fill(arrb, diff)
    elif len(arra) < len(arrb):
        fill(arra, diff)

    # 删除共同前缀（从最高位开始）
    # 注意：原代码在循环中多次调用 check()，逻辑等价于只看第一位是否相同
    while arra and arrb and check() == 1:
        arra.pop(0)
        arrb.pop(0)

    # 将剩下的位数转换为整数（这是原逻辑实现的功能）
    for _ in range(len(arra)):
        ans += temp
        temp *= 2

    return ans


# 如需直接运行示例：
if __name__ == "__main__":
    # 示例：规模为 10
    # print(main(10))
    pass