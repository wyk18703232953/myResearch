import random
import string

def main(n, k=None, seed=0):
    """
    将原始逻辑封装为 main(n, k)。
    自动生成一串长度为 n 的小写字母作为测试数据。
    :param n: 字符串长度
    :param k: 需要选择的字符个数；若为 None，则取 n//2（至少为 1）
    :param seed: 随机种子，保证复现性
    """
    if n <= 0:
        print(-1)
        return

    if k is None:
        k = max(1, n // 2)

    random.seed(seed)
    # 生成长度为 n 的随机小写字母串
    l = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 原始逻辑开始（仅将 input 改为使用 l、n、k）
    chars = sorted(l)
    ans = chars[0]
    ssum = ord(chars[0])
    index = 0

    for j in range(1, n):
        if len(ans) < k:
            if ord(chars[j]) - ord(chars[index]) > 1:
                ans += chars[j]
                ssum += ord(chars[j])
                index = j
        else:
            break

    if len(ans) == k:
        ssum = ssum - 96 * k
        print(ssum)
    else:
        print(-1)

# 示例调用（提交平台通常会自己调用 main，这里仅作为说明）：
# main(10, 3)