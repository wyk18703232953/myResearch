import random
import string

def main(n: int):
    # 随机生成参数 k，取值范围 [1, n]，避免无解的极端情况
    k = random.randint(1, max(1, n))

    # 随机生成长度为 n 的字符串 s，字符集为小写字母
    charset = string.ascii_lowercase
    s = ''.join(random.choice(charset) for _ in range(n))

    flag = True
    lenn = 10**10
    ans = ""

    # 原逻辑：枚举 i 构造 s1，并统计 s 在 s1 中出现次数
    for i in range(n):
        s1 = s + s[n - i - 1:] * (k - 1)
        cnt = 0
        for j in range(len(s1) - len(s) + 1):
            if s1[j:j + len(s)] == s:
                cnt += 1
        if cnt == k and len(s1) < lenn:
            ans = s1
            lenn = len(s1)

    print(ans)


if __name__ == "__main__":
    # 示例调用：可以根据需要调整 n 的默认值或从其他入口传递
    main(5)