import random

def main(n):
    # 随机生成隐藏的 A, B （规模由 n 控制）
    # 假设 A, B 均在 [0, 2^n) 内
    max_val = 1 << n
    hidden_A = random.randrange(max_val)
    hidden_B = random.randrange(max_val)

    # 定义交互函数：根据两个数与 (A,B) 的大小关系返回 -1 / 0 / 1
    # 这里采用常见约定：
    #   return  1  if (x ^ A) > (y ^ B)
    #   return -1  if (x ^ A) < (y ^ B)
    #   return  0  if 相等
    def ask(x, y):
        val1 = x ^ hidden_A
        val2 = y ^ hidden_B
        if val1 > val2:
            return 1
        elif val1 < val2:
            return -1
        else:
            return 0

    a = b = 0
    cond = ask(a, b)
    for i in range(29, -1, -1):
        if cond:
            x = a + (1 << i)
            y = b + (1 << i)
            n_cond = ask(x, y)
            if cond == n_cond:
                if cond == 1:
                    n_cond1 = ask(x, b)
                else:
                    n_cond1 = ask(a, y)

                if cond != n_cond1:
                    a = x
                    b = y
            else:
                if cond == 1:
                    a = x
                else:
                    b = y
                cond = ask(a, b)
        else:
            x = a + (1 << i)
            y = b + (1 << i)
            n_cond = ask(x, b)
            if n_cond == -1:
                a = x
                b = y

    # 输出推断结果和真实答案以便测试
    print("n =", n)
    print("hidden_A =", hidden_A, "hidden_B =", hidden_B)
    print("found_a  =", a, "found_b  =", b)
    print("correct =", (hidden_A == a and hidden_B == b))


if __name__ == "__main__":
    # 示例：调用 main(10)，可自行修改
    main(10)