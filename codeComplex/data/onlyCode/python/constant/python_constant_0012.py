"""
Codeforces
5D - Follow Traffic Rules
http://codeforces.com/contest/5/problem/D

Héctor González Belver
../07/2018
"""
import sys

def time_distance(v0, a, d):
  #quadratic equation. Time is positive ==> root with (+discriminant) in quadratic formula
  #d = v0*t + (a/2)*t^2
  return (-v0 + (v0**2 + 2*a*d)**0.5)/a

def time_accelerating(v0, v1, a):
  return (v1 - v0)/a

def time_speed(v, d):
  return d/v

def distance_travelled(v0, t, a):
  return v0*t + (a/2)*t**2
  
def main():
  a, v = map(int,sys.stdin.readline().strip().split())
  l, d, w = map(int,sys.stdin.readline().strip().split())

  time = 0

  time_to_d = time_distance(0, a, d)
  time_to_v = time_accelerating(0, v, a)

  if (v if time_to_v <= time_to_d else time_to_d * a) <= w:
    #Accelerating 0-v
    acceleration_time = time_to_v
    acceleration_distance = distance_travelled(0, acceleration_time, a)

    if acceleration_distance >= l:
      #Accelerating 0-?
      time = time_distance(0, a, l)
    else:
      #Accelerating 0-v
      time = acceleration_time
      #Max speed v
      time += time_speed(v, l - acceleration_distance)

  else:      
    if time_to_v <= time_to_d:
      #Accelerating 0-v
      acceleration_time = time_to_v
      acceleration_distance = distance_travelled(0, acceleration_time, a)

      #Decelerating v-w
      deceleration_time = time_accelerating(v, w, -a)
      deceleration_distance = distance_travelled(v, deceleration_time, -a)
    
    if time_to_v > time_to_d or acceleration_distance + deceleration_distance > d:
      #Accelerating 0-w
      acceleration_time = time_accelerating(0, w, a)
      acceleration_distance = distance_travelled(0, acceleration_time, a)
      
      remaining_distance = d - acceleration_distance
      #Remaining distance --> Acceleration = -Deceleration ==> half remaining distance each action 
      delta_time = time_distance(w, a, remaining_distance/2)
      #Accelerating 0-? and Decelerating ?-w
      time = acceleration_time + 2*delta_time
    else:
      #Accelerating 0-v
      time = time_to_v
      #Max speed v
      time += time_speed(v, d - deceleration_distance - acceleration_distance)
      #Decelerating v-w
      time += deceleration_time
      
    #Accelerating w-v
    acceleration_time = time_accelerating(w, v, a)
    acceleration_distance = distance_travelled(w, acceleration_time, a)
    if acceleration_distance >= l - d:
      #Accelerating w-?
      time += time_distance(w, a, l - d)
    else:
      #Accelerating w-v
      time += acceleration_time
      #Max speed v
      time += time_speed(v, l - (d + acceleration_distance))
  
  sys.stdout.write('{0:.5f}'.format(time) + '\n')

if __name__ == '__main__': 
  main()