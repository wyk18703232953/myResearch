from random import randint

def main(n):
    """
    n 为规模参数，用来控制测试数据的大小范围。
    这里我们根据 n 生成：
      a: 1 到 (10^n - 1) 之间的随机整数
      b: 在 [a, 10^n - 1] 之间的随机整数（保证有解更容易出现）
    然后执行原程序的逻辑。
    """
    if n <= 0:
        n = 1
    max_val = 10 ** n - 1

    # 生成测试数据
    a = randint(1, max_val)
    b = randint(a, max_val)  # 让 b >= a，便于产生较长答案

    # 原逻辑开始
    ans = ''
    c = sorted(list(str(a)))

    while c:
        for i in range(len(c) - 1, -1, -1):
            # 尝试把 c[i] 放在当前位置，剩余数字保持原顺序
            candidate_digits = list(ans) + [c[i]] + c[:i] + c[i + 1:]
            candidate_val = int(''.join(candidate_digits))
            if candidate_val <= b:
                ans += c[i]
                c.pop(i)
                break

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3 位规模的数据并运行
    main(3)