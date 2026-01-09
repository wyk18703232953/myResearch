import math

def main(n):
    # 生成确定性的输入数组 a，长度为 n
    # a[i] = (i+1)^2 作为示例，保证是整数且随规模变化
    a = [ (i + 1) * (i + 1) for i in range(n) ]
    q = len(a)

    earliest_time = 10**9 + 1000
    earliest_queue = 1
    for i in range(q):
        k = int(max(0, math.ceil((a[i] + 1 - (i + 1)) / q)))
        t = (i + 1) + k * q
        if t < earliest_time:
            earliest_time = t
            earliest_queue = i + 1

    return earliest_queue

if __name__ == "__main__":
    # 示例：以 n = 10 作为规模调用
    result = main(10)
    # print(result)
    pass