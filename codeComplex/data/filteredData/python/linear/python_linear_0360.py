from typing import List
import random

mod = int(1e9 + 7)
maxx = float('inf')


def solve_from_digits(arr: List[int]) -> int:
    """
    原 solve() 的核心逻辑：
    输入：一串数字（每个都是 0~9 的整数），按原题逻辑分段计数。
    返回：分出来的段数 ans。
    """
    s, cnt, ans = 0, 0, 0
    for i in arr:
        s += i
        cnt += 1
        if i % 3 == 0 or cnt % 3 == 0 or s % 3 == 0:
            s, cnt = 0, 0
            ans += 1
    return ans


def main(n: int) -> None:
    """
    生成规模为 n 的测试数据并运行算法。
    这里按照原程序预期，将一串数字当作字符串读入，然后逐位转换为 int。
    因此测试数据为长度为 n 的数字串（每个为 0~9）。
    """
    # 生成测试数据：长度为 n 的数字数组（0~9）
    digits = [random.randint(0, 9) for _ in range(n)]

    # 调用原逻辑
    ans = solve_from_digits(digits)

    # 输出结果
    print(ans)


if __name__ == "__main__":
    # 示例：自行修改 n 测试规模
    main(10)