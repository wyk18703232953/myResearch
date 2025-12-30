from collections import Counter
import random
import string

def main(n: int):
    # 1. 生成测试数据字符串 a、b
    # 这里示例：从小写字母中随机生成长度为 n 的字符串 a、b
    # 你可以按需求修改生成规则
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    b = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # ====== 原始逻辑开始（去掉 input，封装为 main(n)）======

    if len(a) < len(b):
        print(''.join(sorted(a)[::-1]))
        return

    # 如果 a 和 b 长度不等，以 a 的长度为 n，b 截断或补齐（这里截断）
    if len(b) != len(a):
        if len(b) > len(a):
            b = b[:len(a)]
        else:
            # 不足则简单重复填充
            b = (b * ((len(a) + len(b) - 1) // len(b)))[:len(a)]

    n = len(a)
    cnt = Counter(a)

    def f(i=0, check=False):
        if i == n:
            return []
        # 按照原代码逻辑：从大到小枚举当前可用字符
        for j in sorted(cnt)[::-1]:
            if (check or j <= b[i]) and cnt[j]:
                cnt[j] -= 1
                res = f(i + 1, check or j < b[i])
                if len(res) + i + 1 == n:
                    res.append(j)
                    return res
                cnt[j] += 1
        return []

    ans = ''.join(f()[::-1])
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)，可以自行修改 n
    main(5)