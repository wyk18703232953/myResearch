import sys
import heapq

def main(n):
    # n 作为每组衣服数量，生成两组确定性的尺码序列
    key = []
    for i in ['S', 'M', 'L']:
        for j in range(4):
            key.append(j * 'X' + i)

    prev = dict().fromkeys(key, 0)
    now = dict().fromkeys(key, 0)

    # 确定性生成第一个序列：按 key 循环生成长度为 n 的序列
    prev_seq = [key[i % len(key)] for i in range(n)]
    # 确定性生成第二个序列：偏移一位的循环序列
    now_seq = [key[(i + 1) % len(key)] for i in range(n)]

    for item in prev_seq:
        prev[item] += 1
    for item in now_seq:
        now[item] += 1

    for k in key:
        temp = min(prev[k], now[k])
        prev[k] -= temp
        now[k] -= temp

    ans = 0
    for k in key:
        ans += now[k]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)