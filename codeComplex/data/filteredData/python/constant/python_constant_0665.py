import random

def judge(a, b, A, B):
    """模拟交互：返回 sign((A ^ a) - (B ^ b))，与原程序 e 的语义一致。"""
    diff = (A ^ a) - (B ^ b)
    if diff > 0:
        return 1
    elif diff < 0:
        return -1
    else:
        return 0

def main(n):
    """
    n 为规模上界：生成 0 <= A, B < 2^n 的随机整数，
    用原逻辑（通过 judge）推回 A, B，并返回 (A, B, guessed_a, guessed_b)。
    """
    if n <= 0 or n > 30:
        n = 30  # 原代码只处理到 30 位

    # 生成测试数据
    A = random.randint(0, (1 << n) - 1)
    B = random.randint(0, (1 << n) - 1)

    # 原程序逻辑（去掉 input/print，改成调用 judge）
    # 初始询问
    e = judge(0, 0, A, B)
    astr = "0" * 30
    bstr = "0" * 30
    abig = e  # sign(A - B)

    for i in range(30):
        if abig == 0:
            # 当前已知 A == B
            a_candidate = int(astr, 2) + (1 << (29 - i))
            b_candidate = int(bstr, 2)
            e = judge(a_candidate, b_candidate, A, B)
            if e == 1:
                # A^a > B^b，不更新
                continue
            else:
                # A^a <= B^b => 相应位置都置 1
                if i < 29:
                    astr = astr[:i] + "1" + astr[i + 1:]
                    bstr = bstr[:i] + "1" + bstr[i + 1:]
                else:
                    astr = astr[:i] + "1"
                    bstr = bstr[:i] + "1"
        else:
            # 当前已知 A != B，abig = sign(A - B)
            a_candidate = int(astr, 2) + (1 << (29 - i))
            b_candidate = int(bstr, 2) + (1 << (29 - i))
            e = judge(a_candidate, b_candidate, A, B)
            if e == -abig:
                # 高位同加 1 使差符号翻转，说明这一位 A 和 B 不同
                if abig == 1:
                    # A > B，说明这一位 B 的原始位为 1
                    if i < 29:
                        bstr = bstr[:i] + "1" + bstr[i + 1:]
                    else:
                        bstr = bstr[:i] + "1"
                else:
                    # A < B，说明这一位 A 的原始位为 1
                    if i < 29:
                        astr = astr[:i] + "1" + astr[i + 1:]
                    else:
                        astr = astr[:i] + "1"

                # 更新当前差的符号
                abig = judge(int(astr, 2), int(bstr, 2), A, B)
            else:
                # 高位同加 1 未改变符号 => 这一位 A 和 B 相同
                a_candidate = int(astr, 2) + (1 << (29 - i))
                b_candidate = int(bstr, 2)
                e = judge(a_candidate, b_candidate, A, B)
                if e == -1:
                    # 提示 A^a < B^b => 这一位都为 1
                    if i < 29:
                        astr = astr[:i] + "1" + astr[i + 1:]
                        bstr = bstr[:i] + "1" + bstr[i + 1:]
                    else:
                        astr = astr[:i] + "1"
                        bstr = bstr[:i] + "1"

    guessed_a = int(astr, 2)
    guessed_b = int(bstr, 2)

    # 返回真实值和推测值，方便测试
    return A, B, guessed_a, guessed_b


if __name__ == "__main__":
    # 示例：运行一轮规模为 30 的测试
    A, B, ga, gb = main(30)
    print("True A,B:", A, B)
    print("Guessed a,b:", ga, gb)
    print("Correct:", (A, B) == (ga, gb))