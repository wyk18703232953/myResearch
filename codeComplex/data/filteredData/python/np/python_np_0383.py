import sys

def get_graph(n):
    graph = []
    for i in range(n):
        # Deterministic generation: bucket i has i+1 elements
        # Values constructed so that structure is stable and non-trivial
        entries = [i * n + j + 1 for j in range(i + 1)]
        graph.append(entries)
    return graph

def chain(target, buckets, reverse_bucket, sum_bucket, bucket_num, val):
    mask = 2**bucket_num
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
            return mask | 2**new_bucket, mem
        elif new_bucket in buckets_seen:
            return None, []
        
        buckets_seen.add(new_bucket)
        mask = mask | 2**new_bucket

        mem.append((rem, bucket_num))
        bucket_num = new_bucket
        val = rem
    return None, []

def helper(chains, mask, mem):
    if mask == 0:
        return []
    if mask in mem:
        return mem[mask]

    for i, chain_obj in enumerate(chains):
        if (mask >> i) & 0:
            continue
        for key in chain_obj:
            if key | mask != mask:
                continue
    
            future = helper(chains, ~key & mask, mem)
            if future is not None:
                mem[mask] = chain_obj[key] + future
                return mem[mask]
    mem[mask] = None
    return None

def solve_internal(buckets):
    reverse_bucket = {}
    sum_bucket = [0] * len(buckets)
    total_sum = 0
    for i, bucket in enumerate(buckets):
        for x in bucket:
            total_sum += x
            sum_bucket[i] += x
            reverse_bucket[x] = i
    
    target = total_sum / len(buckets) if len(buckets) > 0 else 0

    chains = []
    for i, bucket in enumerate(buckets):
        seto = {}
        for x in bucket:
            key, val = chain(target, buckets, reverse_bucket, sum_bucket, i, x)
            if key is not None:
                seto[key] = val
        chains.append(seto)
    return helper(chains, 2 ** len(buckets) - 1 if len(buckets) > 0 else 0, {}), reverse_bucket

def main(n):
    if n <= 0:
        return
    buckets = get_graph(n)
    res, reverse_bucket = solve_internal(buckets)
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

if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(4)