from collections import Counter
import random

def main(n):
    """
    n: 测试用例个数
    逻辑说明：
    - 原程序读入 testcase，然后对每个用例读一行（无用）和一行数据。
    - 这里我们根据 n 生成 n 组测试数据，每组数据模拟“第二行”的内容。
    - 每组数据长度设为 size（可根据需要调整），元素为 1~max_val 的随机整数。
    """
    random.seed(0)

    testcase = n
    size = 20        # 每个测试用例的数据长度，可根据需要调节
    max_val = 10     # 数值范围 1..max_val，可根据需要调节

    # 生成与原 A[t*2+1] 对应的数据列表
    A = []
    for _ in range(testcase):
        arr = [random.randint(1, max_val) for _ in range(size)]
        A.append(arr)

    # 原逻辑：对每个测试用例的 A[t*2+1] 进行处理
    for t in range(testcase):
        arr = A[t]
        counter = Counter(arr)
        LIST = []

        for c in counter:
            if counter[c] >= 4:
                print(c, c, c, c)
                break
            elif counter[c] >= 2:
                LIST.append(c)
        else:
            LIST.sort()
            # 假设至少有两个出现次数 >=2 的数（与原题类似约束）
            ANS = [LIST[0], LIST[1], LIST[1] / LIST[0]]
            for i in range(2, len(LIST)):
                ratio = LIST[i] / LIST[i - 1]
                if ratio < ANS[2]:
                    ANS = [LIST[i - 1], LIST[i], ratio]

            print(ANS[0], ANS[0], ANS[1], ANS[1])


if __name__ == "__main__":
    # 示例：运行 3 组测试
    main(3)