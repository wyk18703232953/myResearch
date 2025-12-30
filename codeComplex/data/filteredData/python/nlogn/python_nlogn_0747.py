import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组 a
    #   - 为了更贴近原题场景，这里生成 0~n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    a.sort()
    a_count = len(a)

    b = list(filter(lambda i: i > 0, a))
    b_count = len(b)

    def resh():
        idx = 1
        while idx < a_count:
            if a[idx] == a[idx - 1] and (a[idx] - 1) in a:
                return 'cslnb'
            idx += 1

        b_sum = sum(b)
        v_sum = sum(range(1, b_count if a_count == b_count else b_count + 1))
        t = max(b_sum - v_sum, 0)
        return 'cslnb' if t % 2 == 0 else 'sjfnb'

    if b_count == 0 or b_count - len(set(b)) > 1 or a_count - b_count > 1:
        print('cslnb')
    else:
        print(resh())


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)