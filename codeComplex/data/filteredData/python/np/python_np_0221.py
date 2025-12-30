import math
import random

def main(n):
    # 生成测试数据
    # 约束参数
    # 为了有一定可行解，随机生成 z 中的元素，范围适中
    z = [random.randint(1, 100) for _ in range(n)]

    # 根据 z 的和来设置合理的 l, r
    total_sum = sum(z)
    # l 在 [0, total_sum//2] 中
    l = random.randint(0, total_sum // 2 if total_sum > 0 else 0)
    # r 在 [l, total_sum]
    r = random.randint(l, total_sum if total_sum > 0 else l)

    # x 在 [0, max(z)-min(z)] 中
    max_z = max(z)
    min_z = min(z)
    x = random.randint(0, max_z - min_z if max_z > min_z else 0)

    count = 0
    # 枚举所有非空子集（原代码从 0 到 2^n-1，其中 0 对应空集，但条件不会计入）
    for i in range(pow(2, len(z))):
        mini = math.inf
        maxa = 0
        j = i
        inde = 0
        sume = 0
        while j > 0:
            if j & 1:
                sume += z[inde]
                maxa = max(maxa, z[inde])
                mini = min(mini, z[inde])
            j = j >> 1
            inde += 1

        if maxa - mini >= x and l <= sume <= r:
            count += 1

    print(count)

# 示例：如果需要运行，可以调用 main(n)
# main(5)