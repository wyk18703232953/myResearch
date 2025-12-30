from random import randint

def main(n):
    # 生成测试数据：长度为 n 的随机数组，元素范围 1~10^9
    a = [randint(1, 10**9) for _ in range(n)]

    b = sorted(a)
    op = 0
    for i in range(n):
        if a[i] == b[i]:
            continue
        op += 1

    if op == 0 or op == 2:
        print('YES')
    else:
        print('NO')


# 示例调用（提交平台一般会自行调用 main 或你可删除以下示例）
if __name__ == "__main__":
    main(5)