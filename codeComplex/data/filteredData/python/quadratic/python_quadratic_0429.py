import random

def main(n: int):
    # 生成长度为 n 的 0/1 序列作为测试数据
    # 可根据需要调整生成策略，这里使用均匀随机
    arr = [random.randint(0, 1) for _ in range(n)]

    # 逻辑与原程序保持一致，只是去掉了输入输出
    if len(set(arr)) == 1:
        print('YES')
        return

    val = sum(arr)
    if val == 0:
        # 全 0 的情况在上面已返回，这里其实不会触发
        print('YES')
        return

    factor = set()
    for i in range(1, int(val ** 0.5) + 1):
        if val % i == 0:
            factor.add(i)
            factor.add(val // i)

    can = False
    for i in factor:
        each = val // i
        if 1 < i <= n:
            idx = 0
            temp = 0
            cnt = 0
            while idx < n:
                if temp + arr[idx] < each:
                    temp += arr[idx]
                elif temp + arr[idx] > each:
                    temp = 0
                else:
                    temp = 0
                    cnt += 1
                idx += 1
            if cnt == i:
                can = True
                break

    print('YES' if can else 'NO')


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)