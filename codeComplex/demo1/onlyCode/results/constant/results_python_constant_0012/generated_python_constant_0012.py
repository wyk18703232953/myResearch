import math
import random

def time_distance(v0, a, d):
    # Solve d = v0*t + (a/2)*t^2 for positive t
    return (-v0 + math.sqrt(v0 * v0 + 2 * a * d)) / a

def time_accelerating(v0, v1, a):
    return (v1 - v0) / a

def time_speed(v, d):
    return d / v

def distance_travelled(v0, t, a):
    return v0 * t + (a / 2.0) * t * t

def solve(a, v, l, d, w):
    time = 0.0

    time_to_d = time_distance(0, a, d)
    time_to_v = time_accelerating(0, v, a)

    if (v if time_to_v <= time_to_d else time_to_d * a) <= w:
        # Case where speed limit w is not restrictive before point d
        acceleration_time = time_to_v
        acceleration_distance = distance_travelled(0, acceleration_time, a)

        if acceleration_distance >= l:
            # Accelerate from 0 up to some speed over distance l
            time = time_distance(0, a, l)
        else:
            # Accelerate 0 -> v then cruise to end
            time = acceleration_time
            time += time_speed(v, l - acceleration_distance)
    else:
        # Case where speed limit w is restrictive at/before point d
        if time_to_v <= time_to_d:
            # Accelerate 0 -> v before d
            acceleration_time = time_to_v
            acceleration_distance = distance_travelled(0, acceleration_time, a)

            # Decelerate v -> w before d
            deceleration_time = time_accelerating(v, w, -a)
            deceleration_distance = distance_travelled(v, deceleration_time, -a)

        if time_to_v > time_to_d or acceleration_distance + deceleration_distance > d:
            # Can't reach v before needing to enforce w at d
            acceleration_time = time_accelerating(0, w, a)
            acceleration_distance = distance_travelled(0, acceleration_time, a)

            remaining_distance = d - acceleration_distance
            # Symmetric accelerate/decelerate around w on remaining distance
            delta_time = time_distance(w, a, remaining_distance / 2.0)
            time = acceleration_time + 2.0 * delta_time
        else:
            # Reach v, cruise, then slow down to w at/before d
            time = time_to_v
            time += time_speed(v, d - deceleration_distance - acceleration_distance)
            time += deceleration_time

        # After point d, accelerate from w to v if possible, then cruise
        acceleration_time = time_accelerating(w, v, a)
        acceleration_distance = distance_travelled(w, acceleration_time, a)
        if acceleration_distance >= l - d:
            # Not enough distance to reach v
            time += time_distance(w, a, l - d)
        else:
            # Reach v and then cruise
            time += acceleration_time
            time += time_speed(v, l - (d + acceleration_distance))

    return time

def generate_test_data(n):
    # Simple deterministic generator based on n
    random.seed(n)
    # a: 1..10, v: 1..20
    a = random.randint(1, 10)
    v = random.randint(1, 20)
    # l: 1..1000 scaled by n, d: 0..l, w: 0..v
    l = random.randint(1, 1000) * max(1, n)
    d = random.randint(0, l)
    w = random.randint(0, v)
    return a, v, l, d, w

def main(n):
    a, v, l, d, w = generate_test_data(n)
    time = solve(a, v, l, d, w)
    print(f"{time:.5f}")

if __name__ == '__main__':
    # Example: run with n = 1
    main(1)