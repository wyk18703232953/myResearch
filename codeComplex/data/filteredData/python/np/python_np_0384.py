import sys

def get_graph(n):
    graph = []
    # Deterministic construction: n buckets, bucket i has i+1 elements
    # Values are simple arithmetic so structure is fixed by n
    for i in range(n):
        # Example: bucket i contains i+1 consecutive integers starting from i
        entries = [i + j for j in range(1, i + 2)]
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

def solve(n):
    buckets = get_graph(n)
    reverse_bucket = {}
    sum_bucket = [0] * len(buckets)
    total_sum = 0
    for i, bucket in enumerate(buckets):
        for x in bucket:
            total_sum += x
            sum_bucket[i] += x
            reverse_bucket[x] = i
    
    if len(buckets) == 0:
        return None, reverse_bucket

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
    if len(buckets) == 0:
        return None, reverse_bucket
    for i in range(2 ** len(buckets) - 1):
        helper(chains, i, mem)
    return helper(chains, 2 ** len(buckets) - 1, mem), reverse_bucket

def result(n):
    res, reverse_bucket = solve(n)
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
    return "\n".join(output_lines)

def main(n):
    # n is the number of buckets; input data is deterministically generated
    out = result(n)
    sys.stdout.write(out + ("\n" if not out.endswith("\n") else ""))

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(4)