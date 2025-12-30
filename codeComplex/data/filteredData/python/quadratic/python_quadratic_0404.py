import random
import string

def main(n):
    # 生成测试数据：长度为 n 的随机小写字符串，k 取一个正整数
    k = random.randint(1, 10)
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    start = -1
    i = 0
    j = 1
    prev = 1

    # 保持与原算法一致的逻辑
    while i < n - 1:
        while j < n:
            if s[i] == s[j]:
                if start == -1:
                    start = j
                    prev = j
                i += 1
                j += 1
            else:
                i = 0
                j = prev + 1
                prev = j
                start = -1
        break

    if start == -1:
        # 没有找到可复用的后缀
        print(s[:n] * k)
    else:
        # 找到从 start 开始的后缀与前缀匹配
        j = n - start
        print(s[:n] + s[j:n] * (k - 1))


# 示例调用：可以根据需要修改 n 的值
if __name__ == "__main__":
    main(5)