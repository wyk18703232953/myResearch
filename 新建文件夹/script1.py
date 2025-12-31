import time
import dis

# 查看字节码
dis.dis(compile("pow(2, k, mod)", "", "eval"))
# 输出会调用 BUILTIN_POW 函数，不是位移操作

# 性能测试
mod = 10**9 + 7

# 测试 O(log k) 特性
for k in [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]:
    start = time.perf_counter()
    for _ in range(10000):
        pow(2, k, mod)
    elapsed = time.perf_counter() - start
    print(f"k={k}, time={elapsed:.6f}s")
# 时间增长不是线性的，符合 O(log k)