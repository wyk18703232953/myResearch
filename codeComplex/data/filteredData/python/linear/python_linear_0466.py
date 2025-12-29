import random

def main(n: int):
    # 1. 根据 n 生成测试数据：长度为 n 的随机 'b'/'w' 序列
    # 你也可以按需改成固定模式或可重复的伪随机序列
    s = [random.choice(['b', 'w']) for _ in range(n)]

    # 2. 将原逻辑封装并执行
    ans = 0
    far = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            far += 1
            continue
        if s[0] != s[-1]:
            s[:i + 1] = s[:i + 1][::-1]
            s[i + 1:] = s[i + 1:][::-1]
            far += 1
        else:
            ans = max(ans, far + 1)
            far = 0
    print(max(far + 1, ans))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)