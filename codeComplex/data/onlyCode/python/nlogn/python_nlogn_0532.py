n, k = map(int, input().split())
v = list(map(int, input().split()))
 
d = {}
ans = 0
 
for x in v:
  num_d, mod_k = len(str(x)), x % k
  d.setdefault(num_d, {}).setdefault(mod_k, []).append(x)
 
for x in v:
  num_d, mod_k = len(str(x)), x % k
  for add, mods in d.items():
    val_mod = (mod_k * 10 ** add) % k
    need_mod = (k - val_mod) % k
    ans += len(mods.get(need_mod, []))
    if need_mod == mod_k and add == num_d:
      ans -= 1
 
print(ans)
