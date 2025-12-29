from collections import defaultdict
import random

def f(b, d):
    fi = int(b[0])
    if len(b) == 1:
        j = fi
        while j >= 0:
            if d[j]:
                return str(j)
            j -= 1
        return ""

    fi = int(b[0])
    s = ""
    if d[fi] > 0:
        d1 = defaultdict(lambda: 0)
        for j in d:
            d1[j] = d[j]
        d1[fi] -= 1
        s = f(b[1:], d1)

    if s != "":
        return str(fi) + s
    else:
        s1 = ""
        j = fi - 1
        while j >= 0:
            if d[j] > 0:
                s1 += str(j)
                d[j] -= 1
                break
            j -= 1
        if s1 == "":
            return ""
        else:
            j = 9
            while j >= 0:
                if d[j] == 0:
                    j -= 1
                else:
                    s1 += str(j)
                    d[j] -= 1
            return s1


def main(n):
    """
    n: 规模参数，表示数字串 a 的长度
    自动生成测试数据 a, b，逻辑同原程序：
    - a: 长度为 n 的随机数字串（允许前导 0）
    - b: 在 [0, 10^n - 1] 范围内随机生成，再转成不带前导零的十进制串
    """
    if n <= 0:
        return ""

    # 生成长度为 n 的数字串 a
    a_digits = [str(random.randint(0, 9)) for _ in range(n)]
    a = "".join(a_digits)

    # 生成 b：0 <= b < 10^n
    # 避免大整数性能问题，这里限制 n 不超过 18，超过时只用 10**18 范围
    max_power_n = min(n, 18)
    upper = 10 ** max_power_n
    b_val = random.randint(0, upper - 1)
    b = str(b_val)

    d = defaultdict(lambda: 0)
    res = []
    for ch in a:
        d[int(ch)] += 1
        res.append(int(ch))
    res.sort(reverse=True)
    for j in range(len(res)):
        res[j] = str(res[j])

    if len(b) > len(a):
        ans = "".join(res)
    else:
        ans = f(b, d)

    # 返回结果字符串，方便测试或调用
    return {
        "a": a,
        "b": b,
        "answer": ans,
    }


if __name__ == "__main__":
    # 示例：规模为 10
    result = main(10)
    print("a =", result["a"])
    print("b =", result["b"])
    print("answer =", result["answer"])