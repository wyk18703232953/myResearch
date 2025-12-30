import random

def main(n: int) -> int:
    # 生成规模为 n 的测试数据，这里假设为 1~10^6 范围内的随机正整数
    a = [random.randint(1, 10**6) for _ in range(n)]

    a.sort()
    s = []
    for q in a:
        for q1 in s:
            if q % q1 == 0:
                break
        else:
            s.append(q)
    # 原程序输出的是 len(s)，这里返回以便调用者使用
    return len(s)


if __name__ == "__main__":
    # 示例：自行指定 n 运行测试
    result = main(10)
    print(result)