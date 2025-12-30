from collections import defaultdict as dd
import random

mod = 10 ** 9 + 7


def main(n: int) -> int:
    """
    生成规模为 n 的测试数据并执行原逻辑。
    返回计算结果（原程序的输出）。
    """
    # 生成测试数据：n 个 1~10^6 的正整数
    a = [random.randint(1, 10 ** 6) for _ in range(n)]

    b = sorted(a)
    c = dd(int)

    ans = 0
    val = 0
    for i in range(n):
        if c[b[i]] == 0:
            val += 1
            # 遍历所有元素，标记能被当前 b[i] 整除的数
            for j in range(n):
                if b[j] % b[i] == 0:
                    c[b[j]] = val

    for key in c:
        ans = max(ans, c[key])

    print(ans)
    return ans


if __name__ == "__main__":
    # 示例调用：规模设为 6，与原输入示例规模一致
    main(6)