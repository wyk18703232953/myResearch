import random
import math

def time_distance(v0, a, d):
    # Solve d = v0*t + (a/2)*t^2 for t > 0
    return (-v0 + math.sqrt(v0 * v0 + 2 * a * d)) / a

def time_accelerating(v0, v1, a):
    return (v1 - v0) / a

def time_speed(v, d):
    return d / v

def distance_travelled(v0, t, a):
    return v0 * t + (a / 2.0) * t * t

def solve(a, v, l, d, w):
    time = 0.0

    time_to_d = time_distance(0.0, a, d)
    time_to_v = time_accelerating(0.0, v, a)

    max_speed_before_d = v if time_to_v <= time_to_d else time_to_d * a

    if max_speed_before_d <= w:
        # Case 1: speed limit w does not constrain before point d
        acceleration_time = time_to_v
        acceleration_distance = distance_travelled(0.0, acceleration_time, a)

        if acceleration_distance >= l:
            # Accelerating from 0 to some speed within the total distance l
            time = time_distance(0.0, a, l)
        else:
            # Accelerate 0 -> v, then drive at constant v
            time = acceleration_time
            time += time_speed(v, l - acceleration_distance)

    else:
        # Case 2: speed limit w is constraining before point d
        if time_to_v <= time_to_d:
            # Accelerating 0 -> v before d
            acceleration_time = time_to_v
            acceleration_distance = distance_travelled(0.0, acceleration_time, a)

            # Decelerating v -> w
            deceleration_time = time_accelerating(v, w, -a)
            deceleration_distance = distance_travelled(v, deceleration_time, -a)
        else:
            acceleration_time = acceleration_distance = 0.0
            deceleration_time = deceleration_distance = 0.0

        if time_to_v > time_to_d or acceleration_distance + deceleration_distance > d:
            # Cannot reach v before d or cannot fit accel+decel to/from v before d
            # Accelerate 0 -> w
            acceleration_time = time_accelerating(0.0, w, a)
            acceleration_distance = distance_travelled(0.0, acceleration_time, a)

            remaining_distance = d - acceleration_distance
            # Symmetric accelerate/decelerate around w for the remaining distance
            delta_time = time_distance(w, a, remaining_distance / 2.0)

            # Accelerating 0 -> w and then accel/decel around w
            time = acceleration_time + 2.0 * delta_time
        else:
            # Accelerate 0 -> v, constant v, then decelerate v -> w before d
            time = time_to_v
            time += time_speed(v, d - deceleration_distance - acceleration_distance)
            time += deceleration_time

        # After d: Accelerate w -> v if possible
        acceleration_time = time_accelerating(w, v, a)
        acceleration_distance = distance_travelled(w, acceleration_time, a)

        if acceleration_distance >= l - d:
            # Cannot reach v after d; accelerate from w to some speed within remaining distance
            time += time_distance(w, a, l - d)
        else:
            # Accelerate w -> v, then constant v
            time += acceleration_time
            time += time_speed(v, l - (d + acceleration_distance))

    return time

def main(n):
    """
    n controls the scale of generated test data.
    We will generate parameters roughly proportional to n.

    Returns:
        list of results for n test cases.
    """
    random.seed(0)
    results = []
    for _ in range(n):
        # Generate a, v, l, d, w with simple constraints:
        # 1 <= a <= 10*n
        # 1 <= v <= 20*n
        # 1 <= d <= l <= 100*n
        # 1 <= w <= v
        a = random.randint(1, max(1, 10 * n))
        v = random.randint(1, max(1, 20 * n))
        l = random.randint(1, max(1, 100 * n))
        d = random.randint(1, l)
        w = random.randint(1, v)

        t = solve(float(a), float(v), float(l), float(d), float(w))
        results.append((a, v, l, d, w, t))

    # Print results in the same numeric format as original solution
    for a, v, l, d, w, t in results:
        print(f"a={a} v={v} l={l} d={d} w={w} -> {t:.5f}")

    return results

if __name__ == '__main__':
    # Example: run with n = 3
    main(3)