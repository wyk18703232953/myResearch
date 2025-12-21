def time_distance(v0, a, d):
    return (-v0 + (v0**2 + 2 * a * d) ** 0.5) / a

def time_accelerating(v0, v1, a):
    return (v1 - v0) / a

def time_speed(v, d):
    return d / v

def distance_travelled(v0, t, a):
    return v0 * t + (a / 2) * t ** 2

def main(n):
    a = max(1, n % 10 + 1)
    v = max(1, (n * 2) % 20 + 1)
    l = max(1, n * 10)
    d = max(1, l // 2)
    w = max(1, (n * 3) % v)

    time = 0.0

    time_to_d = time_distance(0, a, d)
    time_to_v = time_accelerating(0, v, a)

    if (v if time_to_v <= time_to_d else time_to_d * a) <= w:
        acceleration_time = time_to_v
        acceleration_distance = distance_travelled(0, acceleration_time, a)
        if acceleration_distance >= l:
            time = time_distance(0, a, l)
        else:
            time = acceleration_time
            time += time_speed(v, l - acceleration_distance)
    else:
        if time_to_v <= time_to_d:
            acceleration_time = time_to_v
            acceleration_distance = distance_travelled(0, acceleration_time, a)
            deceleration_time = time_accelerating(v, w, -a)
            deceleration_distance = distance_travelled(v, deceleration_time, -a)
        if time_to_v > time_to_d or acceleration_distance + deceleration_distance > d:
            acceleration_time = time_accelerating(0, w, a)
            acceleration_distance = distance_travelled(0, acceleration_time, a)
            remaining_distance = d - acceleration_distance
            delta_time = time_distance(w, a, remaining_distance / 2)
            time = acceleration_time + 2 * delta_time
        else:
            time = time_to_v
            time += time_speed(v, d - deceleration_distance - acceleration_distance)
            time += deceleration_time
        acceleration_time = time_accelerating(w, v, a)
        acceleration_distance = distance_travelled(w, acceleration_time, a)
        if acceleration_distance >= l - d:
            time += time_distance(w, a, l - d)
        else:
            time += acceleration_time
            time += time_speed(v, l - (d + acceleration_distance))
    return float(f"{time:.5f}")

if __name__ == "__main__":
    print(main(10))