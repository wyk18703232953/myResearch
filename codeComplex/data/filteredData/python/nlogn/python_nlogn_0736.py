import random

def main(n: int):
    # 生成测试数据：n 个非负整数
    # 为了更贴近原题（类似博弈+排序），生成范围控制在 [0, n*2]
    a = [random.randint(0, n * 2) for _ in range(n)]
    a.sort()

    if not any(a):
        print('cslnb')
        return
    if n > 2 and a[0] == a[1] == 0:
        print('cslnb')
        return

    seq_cnt = 0
    seq_sz = 1
    max_seq_sz = 1

    for i in range(n - 1):
        if a[i] == a[i + 1]:
            seq_sz += 1
        elif a[i] + 1 == a[i + 1] and i + 2 < n and a[i + 1] == a[i + 2]:
            max_seq_sz = 3
            break
        else:
            max_seq_sz = max(seq_sz, max_seq_sz)
            seq_cnt += seq_sz > 1
            seq_sz = 1

    max_seq_sz = max(seq_sz, max_seq_sz)
    seq_cnt += seq_sz > 1

    if max_seq_sz > 2 or seq_cnt > 1:
        print('cslnb')
        return

    last = 0
    to_play = 0
    for i in range(n):
        to_play += a[i] - last
        last += 1

    if to_play % 2 == 0:
        print('cslnb')
    else:
        print('sjfnb')


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)