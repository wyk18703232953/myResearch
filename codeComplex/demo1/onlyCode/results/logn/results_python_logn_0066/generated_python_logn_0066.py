def main(n):
    # 生成两组测试数据：0 <= a,b < 2^n
    # 这里简单取 a = 2^n - 1, b = 2^(n-1) 作为示例
    a = (1 << n) - 1
    b = (1 << (n - 1)) if n > 0 else 0

    arra = []
    arrb = []

    # 递归转换为二进制（高位在前）
    def Engine1(num):
        if num > 1:
            Engine1(num // 2)
        arra.append(num % 2)

    def Engine2(num):
        if num > 1:
            Engine2(num // 2)
        arrb.append(num % 2)

    def fill(target_list):
        # 在前面补零，使其长度达到 n
        for _ in range(n):
            target_list.insert(0, 0)

    def check():
        for i, j in zip(arra, arrb):
            if i == j:
                return 1
            else:
                return 0

    # 按原逻辑执行
    Engine1(a)
    Engine2(b)

    diff = abs(len(arra) - len(arrb))
    if len(arra) > len(arrb):
        fill(arrb)
    elif len(arra) < len(arrb):
        fill(arra)

    temp = 1
    ans = 0

    # 注意：原始代码这里使用 range(len(arra))，但在循环中 pop(0)，
    # 实际运行时长度会变化，这会导致逻辑依赖动态变化的 arra/arrb。
    # 为保持与原逻辑一致，固定使用当前长度的次数。
    loop_count = len(arra)
    for _ in range(loop_count):
        if check() == 0:
            break
        check()
        if arra:
            arra.pop(0)
        if arrb:
            arrb.pop(0)

    for _ in range(len(arra)):
        ans += temp
        temp *= 2

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)