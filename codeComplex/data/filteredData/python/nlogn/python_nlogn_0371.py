import random

def main(n: int):
    # 生成测试数据
    # 保证 n >= 1
    if n <= 0:
        return 0

    # 随机生成 K 和数组 A
    # K 取 1~10 之间的整数
    K = random.randint(1, 10)
    # A 中元素取 0~100 之间的整数
    A = [random.randint(0, 100) for _ in range(n)]

    # 原逻辑开始
    A.sort()
    s = []
    for a in A:
        if not s:
            s.append(a)
            continue
        while s:
            if a - K <= s[-1] < a:
                s.pop()
            else:
                break
        s.append(a)
    # 输出结果
    print(len(s))

if __name__ == "__main__":
    # 举例执行 main，n 可按需修改
    main(10)