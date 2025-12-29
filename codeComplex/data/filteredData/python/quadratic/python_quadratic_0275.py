import random

def main(n: int):
    # 生成两个长度为 n 的整数列表，元素范围可按需调整
    a = n
    b = n
    c = [random.randint(1, 100) for _ in range(a)]
    d = [random.randint(1, 100) for _ in range(b)]

    e = []
    for i in c:
        if i in d:
            e.append(i)
    for j in e:
        print(j, end=" ")

if __name__ == "__main__":
    # 示例：n=10，可按需修改或在外部调用 main(n)
    main(10)