import random
import string

def main(n: int):
    # 1. 生成包含重复子串的测试数据 S，长度为 n
    # 目标：保证存在至少一个重复子串，便于测试逻辑
    if n <= 2:
        # 长度太小时直接随机
        S = ''.join(random.choice(string.ascii_lowercase) for _ in range(max(1, n)))
    else:
        # 先生成一个较短的随机串 base，然后在 S 中多次使用
        base_len = max(1, n // 4)
        base = ''.join(random.choice(string.ascii_lowercase) for _ in range(base_len))
        # 构造 S：重复 base，剩余部分随机补齐
        repeat_times = max(2, n // base_len)  # 至少重复两次
        S_list = []
        for _ in range(repeat_times):
            S_list.append(base)
        S = ''.join(S_list)
        # 截断或随机补足到长度 n
        if len(S) > n:
            S = S[:n]
        elif len(S) < n:
            S += ''.join(random.choice(string.ascii_lowercase) for _ in range(n - len(S)))

    # 2. 原始逻辑：在 S 中找出现至少两次的最长子串长度
    best = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            s = S[i:j]
            c = 0
            for k in range(len(S)):
                if S[k:].startswith(s):
                    c += 1
            if c >= 2:
                best = max(best, len(s))

    # 3. 输出结果（可根据需要同时输出 S 以便检查）
    print(best)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(20)