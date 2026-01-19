import itertools

kol1 = {'+': 0, '-': 0, '?': 0}
kol2 = {'+': 0, '-': 0, '?': 0}

s1 = input()
s2 = input()

for s in s1:
    kol1[s] += 1

for s in s2:
    kol2[s] += 1

if (kol1['+']==kol2['+'] and kol1['-']==kol2['-']):
    print('1.0')
    exit()

mod1 = kol1['+'] - kol1['-']
mod2 = kol2['+'] - kol2['-']
mod3 = abs(mod2-mod1)
if (mod3>kol2['?']):
    print(0.0)
    exit()

list_comb = [1, -1]
sum_pos = 0
col = 0
# import pdb; pdb.set_trace()
for comb in itertools.product(list_comb, repeat=kol2['?']):
    if sum(comb)==mod3:
        sum_pos += 1
    col+=1

print(sum_pos/col)