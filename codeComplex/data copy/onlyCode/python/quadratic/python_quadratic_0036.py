n = int(input().rstrip())
arr = []
mod = pow(10,9) + 7
indent_num = 0
for i in range(n):
    arr.append(input().rstrip())
    if arr[i] == 'f':
        indent_num += 1
dp = [0 for i in range(indent_num + 1)]
first_block_index = 0
max_indent = 0
for i in arr:
    if i != 'f':
        break
    first_block_index += 1
    max_indent += 1

dp[max_indent] = 1
#print(dp)
cur_indent = 0
pref = [0 for i in range(indent_num + 1)]
def cal_pref(dp, pref):
    pref[0] = dp[0]
    for i in range(1, len(dp)):
        pref[i] = pref[i - 1] + dp[i]

for i in range(first_block_index + 1,n):
    if arr[i] == 'f':
        cur_indent += 1
        max_indent += 1
        continue
   
    cur = [0 for i in range(indent_num + 1)]
    cal_pref(dp, pref)
    for j in range(cur_indent,indent_num + 1):
        res_idx = j - cur_indent
        res_result = pref[res_idx - 1] if res_idx > 0 else 0
        cur[j] = (pref[indent_num] - res_result) % mod
        #cur[j] = sum(dp[j - cur_indent:indent_num + 1]) % mod
    cur[max_indent] = 1 if not cur[max_indent] else cur[max_indent]
    dp = cur
    cur_indent = 0
    #print(i,arr[i], dp)


print(sum(dp) % mod)
