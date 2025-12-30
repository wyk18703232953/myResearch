import random

def main(n):
    # 生成测试数据
    # n: lst1 的规模，同时也作为 lst2 的规模
    # 元素范围 [1, 2*n]，保证有交集也可能有不在 lst1 中的元素
    lst1 = [random.randint(1, 2 * n) for _ in range(n)]
    lst2 = [random.randint(1, 2 * n) for _ in range(n)]

    # 原逻辑开始
    lst3 = {}
    ans = []
    for i in lst2:
        if i in lst1:
            lst3[i] = lst1.index(i)
    for i in sorted(lst3, key=lst3.get):
        ans.append(i)
    print(*ans, sep=" ")

if __name__ == "__main__":
    # 可根据需要修改规模
    main(10)