import random
import sys


def get_graph_from_data(n, data):
    graph = []
    for i in range(n):
        # 原程序读取时会丢弃每行的第一个数，这里模拟同样的行为：
        # 每一行的格式类似：k a1 a2 ... ak，实际只使用后面的值
        entries = data[i][1:]  # data[i] 已经是整数列表
        graph.append(entries)
    return graph


def chain(target, buckets, reverse_bucket, sum_bucket, bucket_num, val):
    mask = 2 ** bucket_num
    mem = []
    buckets_seen = set({bucket_num})

    og_bucket = bucket_num
    og_val = val
    for _ in range(len(buckets)):
        rem = target - sum_bucket[bucket_num] + val
        if rem not in reverse_bucket:
            return None, []

        new_bucket = reverse_bucket[rem]
        if new_bucket == og_bucket and rem != og_val:
            return None, []
        elif new_bucket == og_bucket and rem == og_val:
            mem.append((rem, bucket_num))
            return mask | 2 ** new_bucket, mem
        elif new_bucket in buckets_seen:
            return None, []

        buckets_seen.add(new_bucket)
        mask = mask | 2 ** new_bucket

        mem.append((rem, bucket_num))
        bucket_num = new_bucket
        val = rem
    return None, []


def helper(chains, mask, mem):
    if mask == 0:
        return []
    if mask in mem:
        return mem[mask]

    for i, chain_map in enumerate(chains):
        if (mask >> i) & 0:
            continue
        for key in chain_map:
            if key | mask != mask:
                continue

            future = helper(chains, ~key & mask, mem)
            if future is not None:
                mem[mask] = chain_map[key] + future
                return mem[mask]
    mem[mask] = None
    return None


def solve_with_buckets(buckets):
    reverse_bucket = {}
    sum_bucket = [0] * len(buckets)
    total_sum = 0
    for i, bucket in enumerate(buckets):
        for x in bucket:
            total_sum += x
            sum_bucket[i] += x
            reverse_bucket[x] = i

    # 为了可与整数索引匹配，target 保持为 float 与原逻辑一致
    target = total_sum / len(buckets)

    chains = []
    for i, bucket in enumerate(buckets):
        seto = {}
        for x in bucket:
            key, val = chain(target, buckets, reverse_bucket, sum_bucket, i, x)
            if key is not None:
                seto[key] = val
        chains.append(seto)
    return helper(chains, 2 ** len(buckets) - 1, {}), reverse_bucket


def generate_test_data(n):
    """
    生成用于算法的测试数据。
    模拟原输入格式：n 行，每行形如：
    k a1 a2 ... ak
    这里简单生成：
    - 每个桶的大小 k 为 1~3 之间随机
    - ai 在 1~20 范围内随机
    """
    random.seed(0)
    data = []
    for _ in range(n):
        k = random.randint(1, 3)
        row = [k]
        for _ in range(k):
            row.append(random.randint(1, 20))
        data.append(row)
    return data


def main(n):
    # 生成数据并构造 buckets（graph）
    data = generate_test_data(n)
    buckets = get_graph_from_data(n, data)

    res, reverse_bucket = solve_with_buckets(buckets)

    if res is None:
        sys.stdout.write("No\n")
    else:
        res = sorted(res, key=lambda x: reverse_bucket[x[0]])
        sys.stdout.write("Yes\n")
        for x, y in res:
            x = int(x)
            y = int(y) + 1
            stuff = " ".join([str(x), str(y), "\n"])
            sys.stdout.write(stuff)


# 示例：直接运行文件时可执行一个规模
if __name__ == "__main__":
    main(4)