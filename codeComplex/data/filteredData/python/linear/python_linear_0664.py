def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return 0

    # Deterministic generation of l (list of integers) and s (string of 'G', 'W', 'L')
    # l[i] = (i % 5) + 1 -> values cycle through 1..5
    l = [(i % 5) + 1 for i in range(n)]

    # s pattern cycles through 'G', 'W', 'L'
    chars = ['G', 'W', 'L']
    s = ''.join(chars[i % 3] for i in range(n))

    water = 0
    grass = 0
    cgrass = 0
    time = 0
    seen = False

    for i in range(n):
        if s[i] == "G":
            dist = l[i]
            if water >= dist:
                water -= dist
                time += 2 * dist
                cgrass += dist

            else:
                dist -= water
                time += 2 * water
                cgrass += water
                water = 0
                time += 3 * dist
                grass += dist
        elif s[i] == "W":
            water += l[i]
            time += 2 * l[i]
            seen = True

        else:
            dist = l[i]
            if water >= dist:
                water -= dist
                time += 2 * dist

            else:
                dist -= water
                time += 2 * water
                water = 0
                if cgrass >= dist:
                    cgrass -= dist
                    grass += dist
                    time += 3 * dist

                else:
                    dist -= cgrass
                    grass += cgrass
                    time += 3 * cgrass
                    cgrass = 0
                    if grass >= dist:
                        grass -= dist
                        time += 3 * dist

                    else:
                        dist -= grass
                        time += 3 * grass
                        grass = 0
                        if seen:
                            time += 4 * dist

                        else:
                            time += 6 * dist

    return time


if __name__ == "__main__":
    # Example deterministic calls for time complexity experiments
    for n in [1, 5, 10, 100, 1000]:
        # print(n, main(n))
        pass