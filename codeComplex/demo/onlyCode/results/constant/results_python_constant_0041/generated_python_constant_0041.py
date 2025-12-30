import random

def main(n: int) -> None:
    # 原逻辑：判断 n 是否“almost lucky”
    m = ''.join(set(list(str(n))))
    if m in ('47', '74', '4', '7'):
        print('YES')
    else:
        if n % 4 == 0 or n % 7 == 0 or n % 74 == 0 or n % 47 == 0:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    # 根据 n 生成测试数据：这里随机生成一个 1 到 10^9 之间的整数作为示例
    # 可根据需要修改 n 的取值规则
    n = random.randint(1, 10**9)
    main(n)