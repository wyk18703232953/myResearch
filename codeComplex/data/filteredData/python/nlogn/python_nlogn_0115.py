import random

def main(n: int):
    # 3. 根据 n 生成测试数据（这里生成 1 到 100 之间的随机整数）
    a = [random.randint(1, 100) for _ in range(n)]

    # 以下为原逻辑
    sortm = a[:]            # 拷贝一份
    sortm.sort()            # 排序

    cnt = 0
    for i in range(n):
        if a[i] != sortm[i]:
            cnt += 1

    if cnt <= 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)