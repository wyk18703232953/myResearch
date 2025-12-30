import random
import string


def main(n: int) -> str:
    # 生成规模为 n 的测试数据：tam, q, 以及长度为 tam 的字符串 t
    # 这里约定：
    #   tam = n
    #   q   = 随机取值 1..n（至少为 1）
    #   t   = 由小写字母组成的长度为 tam 的随机字符串
    if n <= 0:
        return ""

    tam = n
    q = random.randint(1, max(1, n))
    t = "".join(random.choice(string.ascii_lowercase) for _ in range(tam))

    s = t
    posi = -1

    # 按原逻辑寻找最长前缀，使得前缀 == 后缀
    for j in range(tam - 1):
        if t[: j + 1] == t[tam - j - 1 :]:
            posi = j

    add = t[posi + 1 :]

    for _ in range(q - 1):
        s += add

    return s


if __name__ == "__main__":
    # 示例: 以 n=10 运行并打印结果
    print(main(10))