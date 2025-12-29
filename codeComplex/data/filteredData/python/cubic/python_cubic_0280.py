import sys as _sys
import random

_sys.setrecursionlimit(2**14)

_cache = dict()


class _SortedSeqs:

    def __init__(self, seqs):
        self.seqs = tuple(tuple(sorted(seq)) for seq in seqs)

    def __hash__(self):
        return id(self)


def compute_max_area(r_seq, g_seq, b_seq):
    sorted_seqs_obj = _SortedSeqs((r_seq, b_seq, g_seq))
    seqs_sizes = tuple(map(len, sorted_seqs_obj.seqs))
    return _compute_max_area(sorted_seqs_obj, seqs_sizes)


def _compute_max_area(sorted_seqs_obj, seqs_sizes):
    cache_key = (sorted_seqs_obj, seqs_sizes)
    if cache_key in _cache.keys():
        return _cache[cache_key]

    seqs = sorted_seqs_obj.seqs
    nonempty_seqs_n = _how_many_nonempty(seqs_sizes)

    if nonempty_seqs_n < 2:
        ab_seqs_indices_list = []

    elif nonempty_seqs_n == 2:
        ab_seqs_indices = [i for i, seq_size in enumerate(seqs_sizes) if seq_size > 0]
        ab_seqs_indices_list = [ab_seqs_indices]

    else:
        assert nonempty_seqs_n == 3
        seqs_indices_sorted_by_size = [
            i for i, seq in sorted(
                enumerate(seqs),
                key=lambda pair: (pair[1][seqs_sizes[pair[0]] - 1], seqs_sizes[pair[0]])
            )
        ]
        ab_seqs_indices_1 = seqs_indices_sorted_by_size[2], seqs_indices_sorted_by_size[0]
        ab_seqs_indices_2 = seqs_indices_sorted_by_size[2], seqs_indices_sorted_by_size[1]
        ab_seqs_indices_list = [ab_seqs_indices_1, ab_seqs_indices_2]

    max_areas_variants = []
    for a_seq_index, b_seq_index in ab_seqs_indices_list:
        a_seq_last = seqs[a_seq_index][seqs_sizes[a_seq_index] - 1]
        b_seq_last = seqs[b_seq_index][seqs_sizes[b_seq_index] - 1]
        new_seqs_sizes = list(seqs_sizes)
        new_seqs_sizes[a_seq_index] -= 1
        new_seqs_sizes[b_seq_index] -= 1
        max_area = _compute_max_area(sorted_seqs_obj, tuple(new_seqs_sizes))
        max_area += a_seq_last * b_seq_last
        max_areas_variants.append(max_area)

    max_area = max(max_areas_variants, default=0)

    _cache[cache_key] = max_area
    return max_area


def _how_many_nonempty(seqs_sizes):
    return len([size for size in seqs_sizes if size > 0])


def main(n):
    # 生成规模为 n 的随机测试数据：
    # 三个序列长度都为 n，元素为 1 到 1000 的随机整数
    r_seq = tuple(random.randint(1, 1000) for _ in range(n))
    g_seq = tuple(random.randint(1, 1000) for _ in range(n))
    b_seq = tuple(random.randint(1, 1000) for _ in range(n))
    result = compute_max_area(r_seq, g_seq, b_seq)
    print(result)


if __name__ == '__main__':
    # 示例：n = 5
    main(5)