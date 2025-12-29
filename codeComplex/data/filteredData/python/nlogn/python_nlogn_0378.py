from collections import Counter
import random

def main(n):
    # 生成测试数据：
    # 随机生成 k 和长度为 n 的数组 li（元素范围可按需调整）
    k = random.randint(0, 10)
    li = [random.randint(0, 100) for _ in range(n)]

    # 下面是原逻辑改写，无 input()
    dic = Counter(li)
    li_unique = sorted(set(li))
    m = len(li_unique)

    for i in range(1, m):
        for j in range(i - 1, -1, -1):
            if li_unique[j] + k >= li_unique[i] and dic[li_unique[j]] != 0:
                dic[li_unique[j]] = 0
            else:
                break

    result = sum(dic.values())
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次运行
    main(10)