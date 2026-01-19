def main(n):
    # Generate s (target string) of length n using a simple deterministic pattern
    # Example pattern: first n//2 are '+', rest are '-'
    s = ''.join('+' if i < n // 2 else '-' for i in range(n))

    # Generate cmd string of length n using a deterministic pattern over '+', '-', '?'
    # Pattern cycles every 3 characters: '+', '-', '?'
    symbols = ['+', '-', '?']
    cmd = ''.join(symbols[i % 3] for i in range(n))

    trgt = 0
    for c in s:
        trgt += (1 if c == '+' else -1)

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
                nextqueue.append([pos + 1, cmdi + 1])
            elif nextcmd == '-':
                nextqueue.append([pos - 1, cmdi + 1])
            else:
                nextqueue.append([pos + 1, cmdi + 1])
                nextqueue.append([pos - 1, cmdi + 1])
        queue = nextqueue

    occurs = 0
    for x in dests:
        if x == trgt:
            occurs += 1

    # To avoid ZeroDivisionError when n == 0 and thus len(dests) == 0
    if len(dests) == 0:
        result = 0.0
    else:
        result = occurs / len(dests)

    print(result)
    return result


if __name__ == "__main__":
    main(5)