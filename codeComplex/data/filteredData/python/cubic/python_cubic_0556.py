import random

def main(n: int):
    # 生成测试数据：
    # a 为长度 n 的数字串，b 为长度 n 的数字串，且 b >= a，保证原逻辑中 num<=b 有合理意义
    # 为简单起见，随机生成 a，然后在其基础上生成一个不小于它的 b
    digits = "0123456789"
    # 保证首位不为 0，避免无意义前导 0 情况
    first_digit_a = random.choice(digits[1:])
    a = first_digit_a + "".join(random.choice(digits) for _ in range(n - 1))

    # 生成 b：随机决定是否等于 a 或稍微变大
    if random.random() < 0.5:
        b = a
    else:
        # 将 a 看作整数加上一个小随机数，保持位数不变的前提下尽量不溢出
        a_int = int(a)
        # 增量控制在 [1, 10^min(3, n)-1] 之间
        inc = random.randint(1, 10 ** min(3, n) - 1)
        b_int = a_int + inc
        # 若发生位数增加，则退回为 a
        if len(str(b_int)) > n:
            b = a
        else:
            b = str(b_int).zfill(n)

    # 以下为原逻辑（去掉 input() 后直接使用 a, b）

    v = sorted(a)
    v = v[::-1]
    x = ""
    for i in range(len(v)):
        x = x + v[i]
    v = x

    if len(a) < len(b):
        print(v)
    else:
        if b == a:
            print(a)
        else:
            fin = ""
            flag = False
            for j in range(len(a)):
                for k in range(len(a)):
                    num = fin + v[k] + "".join(sorted(v[:k] + v[k + 1 :]))
                    if num <= b:
                        fin += v[k]
                        if int(v[k]) < int(b[j]):
                            flag = True
                            v = v[:k] + v[k + 1 :]
                            fin += v
                        v = v[:k] + v[k + 1 :]
                        break
                if flag:
                    break
            print(fin)


if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)