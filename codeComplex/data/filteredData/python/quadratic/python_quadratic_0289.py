import random

def main(n: int) -> int:
    # 生成测试数据：随机长度为 n、元素范围 [0, n-1] 的列表
    l = [random.randint(0, n - 1) for _ in range(n)]
    ans = 0
    while len(l) > 0:
        a = l[0]
        l = l[1:]
        if a in l:
            ans += l.index(a)
            l.remove(a)
        else:
            # 原代码在找不到 a 时会抛异常，这里选择跳过保持运行
            pass
    return ans

if __name__ == "__main__":
    # 示例：自行设定规模测试
    result = main(10)
    print(result)