s = input()
trgt = 0
for c in s:
    trgt += (1 if c == '+' else -1)

cmd = input()

queue = [[0, 0]]
dests = []

while queue:
    nextqueue = []
    for pos, cmdi in queue:
        if cmdi == len(cmd):
            dests.append(pos)
            continue
        nextcmd = cmd[cmdi]
        if nextcmd == '+':
            nextqueue.append([pos+1, cmdi+1])
        elif nextcmd == '-':
            nextqueue.append([pos-1, cmdi+1])
        else:
            nextqueue.append([pos + 1, cmdi + 1])
            nextqueue.append([pos - 1, cmdi + 1])
    queue = nextqueue

occurs = 0
for x in dests:
    if x == trgt:
        occurs+=1
print(occurs / len(dests))