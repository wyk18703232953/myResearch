#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main(n):
    # 生成规模为 n 的确定性输入
    # 原程序第一行读但未使用，这里省略
    # 原 a 为整数列表，这里构造一个包含重复元素的确定性序列
    a = [(i // 2) for i in range(n)]
    # 对应原始逻辑从这里开始
    a.sort()
    cnt = 0
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            a[i] -= 1
            cnt += 1
            break
    if a and a[0] < 0:
        # print('cslnb')
        pass
        return

    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            # print('cslnb')
            pass
            return

    for i, x in enumerate(a):
        cnt += x - i

    # print('sjfnb' if (cnt & 1) else 'cslnb')
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 以做时间复杂度实验
    main(10)