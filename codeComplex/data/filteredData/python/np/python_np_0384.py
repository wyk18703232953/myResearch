import sys
import random


def get_graph_from_data(data):
    graph = []
    for row in data:
        # row is list of ints; first elem is count (ignored), rest are bucket values
        entries = row[1:]
        graph.append(entries)
    return graph


def chain(target, buckets, reverse_bucket, sum_bucket, bucket_num, val):
    mask = 2 ** bucket_num
    mem = []
    buckets_seen = {bucket_num}

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

    for i, chain_dict in enumerate(chains):
        if (mask >> i) & 0:
            continue
        for key in chain_dict:
            if key | mask != mask:
                continue

            future = helper(chains, ~key & mask, mem)
            if future is not None:
                mem[mask] = chain_dict[key] + future
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

    target = total_sum / len(buckets)

    chains = []
    for i, bucket in enumerate(buckets):
        seto = {}
        for x in bucket:
            key, val = chain(target, buckets, reverse_bucket, sum_bucket, i, x)
            if key is not None:
                seto[key] = val
        chains.append(seto)
    mem = {}
    for i in range(2 ** len(buckets) - 1):
        helper(chains, i, mem)
    return helper(chains, 2 ** len(buckets) - 1, mem), reverse_bucket


def generate_test_data(n, seed=0):
    """
    生成符合原程序输入格式的测试数据：
    - n 行，每行：k_i v_1 v_2 ... v_k_i
    - k_i >= 1
    - 尝试生成总和可被 n 整除，使得有较大概率存在解
    """
    random.seed(seed)
    data = []

    # 每个桶的大小在 [1, min(5, n)] 之间
    for _ in range(n):
        k = random.randint(1, min(5, max(1, n)))
        # 值在 [-10*n, 10*n] 范围内
        vals = [random.randint(-10 * n, 10 * n) for _ in range(k)]
        data.append([k] + vals)

    # 可选：微调使得总和更容易被 n 整除
    total_sum = sum(v for row in data for v in row[1:])
    remainder = total_sum % n
    if remainder != 0:
        # 在第一行修改一个数以调整总和
        # 确保第一行有至少一个元素
        adjust = (-remainder)
        data[0][1] += adjust

    return data


def result_from_buckets(buckets):
    res, reverse_bucket = solve_with_buckets(buckets)
    output_lines = []
    if res is None:
        output_lines.append("No")
    else:
        res = sorted(res, key=lambda x: reverse_bucket[x[0]])
        output_lines.append("Yes")
        for x, y in res:
            x = int(x)
            y = int(y) + 1
            output_lines.append(f"{x} {y}")
    return "\n".join(output_lines) + "\n"


def main(n):
    """
    n 为桶的数量，根据 n 生成测试数据并运行原逻辑。
    直接打印结果到 stdout，并返回结果字符串。
    """
    data = generate_test_data(n)
    buckets = get_graph_from_data(data)
    res_str = result_from_buckets(buckets)
    sys.stdout.write(res_str)
    return res_str


if __name__ == "__main__":
    # 示例：运行 main(4)
    main(4)