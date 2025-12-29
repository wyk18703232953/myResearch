import random

def main(n: int):
    # 生成一棵有 n 个节点的树（节点编号 1..n，1 为根）
    # 对于每个节点 i(2..n)，随机指定一个父节点 v(1..i-1)
    # 这样一定是棵树
    t = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        v = random.randint(1, i - 1)
        t[v].append(i)

    flag = True
    for children in t:
        if children:
            cnt = 0
            for child in children:
                if not t[child]:  # 叶子结点
                    cnt += 1
            if cnt < 3:
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：规模 n = 10，可按需修改
    main(10)