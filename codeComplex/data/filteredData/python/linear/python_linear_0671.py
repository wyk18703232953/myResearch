import random

def main(n):
    # 根据规模 n 生成测试数据，这里生成 0~100 的随机整数
    a = [random.randint(0, 100) for _ in range(n)]
    
    b = 0
    for i in range(n):
        if a[i] % 2 == 1:
            if i % 2 == 0:
                b += 1
            else:
                b -= 1

    if n % 2 == 0:
        if b == 0:
            print("YES")
        else:
            print("NO")
    else:
        if b == 0 or b == 1:
            print("YES")
        else:
            print("NO")

# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)