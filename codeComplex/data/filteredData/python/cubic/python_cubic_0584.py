from string import digits
from collections import Counter
import random


def solve(a: str, b: str) -> str:
    ca = Counter(a)
    l = []

    if len(b) > len(a):
        # 直接用所有数字从大到小排
        for i in digits[::-1]:
            if i in ca:
                l.extend(i * ca[i])
    else:
        def dfs(i: int, smaller: bool) -> bool:
            # i: 当前处理到 b 的第 i 位
            # smaller: 当前构造的前缀是否已经小于 b 的前缀
            if i == len(b):
                return True
            if smaller:
                # 已经比 b 小了，后面随便最大
                for j in digits[::-1]:
                    if j in ca and ca[j] > 0:
                        l.extend(j * ca[j])
                return True
            else:
                # 前缀仍然等于 b 的前缀，只能放 <= b[i] 的数
                upper = int(b[i])
                for j in digits[:upper + 1][::-1]:
                    if j in ca and ca[j] > 0:
                        ca[j] -= 1
                        l.append(j)
                        if dfs(i + 1, j != b[i]):
                            return True
                        # 回溯
                        ca[j] += 1
                        l.pop()
                return False

        dfs(0, False)

    return "".join(l)


def main(n: int):
    """
    n: 控制规模，这里用作字符串长度上限。
    生成测试数据 a, b 后，输出对应结果。
    """
    if n <= 0:
        return

    # 随机生成长度
    len_a = random.randint(1, n)
    len_b = random.randint(1, n)

    # 随机生成数字串 a, b
    a = "".join(random.choice(digits) for _ in range(len_a))
    b = "".join(random.choice(digits) for _ in range(len_b))

    # 输出输入数据与结果，便于测试
    print("a =", a)
    print("b =", b)
    ans = solve(a, b)
    print("result =", ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)