import random

def main(n):
    # 生成测试数据：n 个 1..n 的随机整数（可按需要调整规则）
    a = [random.randint(1, n) for _ in range(n)]
    ans = 0
    # 为了不修改原始列表，可以做一次拷贝（按需）
    arr = a[:]
    while len(arr) > 0:
        c = arr.pop(0)
        # 若列表中有多个 c，index 取第一个；与原始逻辑一致
        i = arr.index(c)
        ans += i
        del arr[i]
    print(ans)