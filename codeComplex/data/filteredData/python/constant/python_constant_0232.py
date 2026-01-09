def main(n):
    # Interpret n as the scale of generated test data.
    # Generate deterministic values for A, B, yellow, green, blue based on n.
    A = n
    B = 2 * n
    yellow = n // 2
    green = n // 3
    blue = n // 4

    yelreq = 0
    blureq = 0

    # for yellow balls
    yelreq = 2 * yellow

    # green balls 
    yelreq += green
    blureq += green

    # blue balls 
    blureq += 3 * blue

    reqs = 0
    if A < yelreq:
        reqs += yelreq - A
    if B < blureq:
        reqs += blureq - B

    # print(reqs)
    pass
if __name__ == "__main__":
    # Example deterministic call
    main(10)