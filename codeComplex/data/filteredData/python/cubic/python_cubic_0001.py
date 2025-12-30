#!/usr/bin/env python
"""
Converted version:
- No input()
- Logic wrapped in main(n) with scalable size n
- Test data (k) generated from n
"""

def main(n):
    # 生成测试数据：根据 n 生成一个 k（原代码中使用的是 0-based 的 k，再加 1）
    # 这里简单生成 k = 2^(max(0, n-2)) // 2，防止过大，同时留一定变化空间
    # 可根据需要自行调整生成规则
    if n <= 2:
        k = 0
    else:
        # 上界只是为了防止某些 n 时组合数过大，影响运行时间
        from math import ceil
        max_k = 1 << max(0, n - 2)
        k = max_k // 2

    # 将原 main 中的逻辑搬到此处，并使用闭包访问 ans
    def num(left, right, dp, rev, revI):
        if left > right:
            return 1

        key = (left, rev, revI)
        if key in dp:
            return dp[key]

        acc = 0

        for x in ('01' if ans[left] == '#' else ans[left]):
            if left == right:
                tmp = x
            elif ans[right] == '#':
                tmp = '01'
            else:
                tmp = ans[right]

            for y in tmp:
                if not ((rev and x > y) or (revI and x == y == '1')):
                    acc += num(
                        left + 1,
                        right - 1,
                        dp,
                        rev and x == y,
                        revI and x != y
                    )
        dp[key] = acc
        return acc

    # 这里的 k 对应原逻辑中的输入 k，再执行 k += 1
    k += 1

    # 初始化 ans
    # ans[i] 为 '0' / '1' 或 '#'（未确定）
    ans = ['#'] * n

    # 尝试逐位确定 ans
    for i in range(n):
        ans[i] = '0'
        tmp = num(0, n - 1, {}, True, True)

        if k > tmp:
            k -= tmp
            ans[i] = '1'

    # 输出结果
    if ans[0] == '0':
        print(''.join(ans))
    else:
        print(-1)


if __name__ == '__main__':
    # 示例：可在此处调用 main(n) 做简单测试
    # 用户可根据需要修改 n
    main(10)