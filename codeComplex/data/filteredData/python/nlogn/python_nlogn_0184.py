from collections import defaultdict
import random

def main(n):
    # 生成规模为 n 的测试数据，这里示例为在 [-10^6,10^6] 区间内的随机整数
    # 如有需要可按题意修改生成规则
    max_abs = 10**6
    a = [random.randint(-max_abs, max_abs) for _ in range(n)]

    dic = defaultdict(int)
    cursum = 0
    ans = 0

    for i in range(n):
        ele = a[i]
        has_l = (ele - 1) in dic
        has_r = (ele + 1) in dic

        if has_l and has_r:
            ans += ele * (i - dic[ele - 1] - dic[ele + 1]) - (
                cursum - (dic[ele - 1] * (ele - 1) + dic[ele + 1] * (ele + 1))
            )
        elif has_l:
            ans += ele * (i - dic[ele - 1]) - (
                cursum - dic[ele - 1] * (ele - 1)
            )
        elif has_r:
            ans += ele * (i - dic[ele + 1]) - (
                cursum - dic[ele + 1] * (ele + 1)
            )
        else:
            ans += ele * i - cursum

        dic[ele] += 1
        cursum += ele

    print(ans)


if __name__ == "__main__":
    # 示例：运行 main 并指定规模 n
    main(10)