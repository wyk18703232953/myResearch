def main(n):
    import math

    # Map n to tree size and k
    if n < 2:
        size = 2

    else:
        size = n
    k = max(1, size // 4)

    # Deterministically generate a tree with 'size' nodes:
    # Use a simple path 1-2-3-...-size to keep structure simple and deterministic.
    edges = [(i, i + 1) for i in range(1, size)]

    # Original logic starts here, with n -> size
    n_local = size

    degreelist = []
    for i in range(min(k + 1, math.floor(math.log2(n_local)) + 10)):
        degreelist.append({})
    degrees = degreelist[0]
    for i in range(1, n_local + 1):
        degrees[i] = 0
    for guy in edges:
        degrees[guy[0]] += 1
        degrees[guy[1]] += 1
    small = []
    center = None
    done = False
    for i in range(k):
        if not done:
            small = []
            for guy in degrees:
                if degrees[guy] == 2:
                    # print("No")
                    pass
                    done = True
                    break
                if degrees[guy] == 3:
                    small.append(guy)
                    if center == None:
                        center = guy
                    elif center != guy:
                        # print("No")
                        pass
                        done = True
                        break
                elif degrees[guy] > 1:
                    small.append(guy)
            degrees = degreelist[i + 1]
            if center != None and center not in small:
                if not done:
                    # print("No")
                    pass
                done = True
                break
            elif len(small) == 0:
                if not done:
                    # print("No")
                    pass
                done = True
                break
            for guy in small:
                degrees[guy] = 0
            for guy in edges:
                if guy[0] in degrees and guy[1] in degrees:
                    degrees[guy[0]] += 1
                    degrees[guy[1]] += 1
            for guy in degrees:
                if degrees[guy] > 1 and degreelist[i][guy] != degrees[guy]:
                    if not done:
                        # print("No")
                        pass
                    done = True
                    break

        else:
            break
    if not done:
        if len(degreelist[-1]) == 1:
            # print("Yes")
            pass

        else:
            # print("No")
            pass
if __name__ == "__main__":
    main(10)