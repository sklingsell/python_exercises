import math

angle = float(input('Please enter the angle (in degrees): '))
velocity = float(input('Please enter the velocity (in km/h): '))
init_height = float(input('Please enter the throw height (in meters): '))

def kmh_to_ms(velocity):
    velocity_mps = velocity/3.6
    return velocity_mps

def velocity_decomposition(velocity,angle):
    angle_radian = math.radians(angle)    
    velocity_mps = kmh_to_ms(velocity)
    velocity_horizontal = velocity_mps * math.cos(angle_radian)
    velocity_vertical = velocity_mps * math.sin(angle_radian)
    return velocity_horizontal,velocity_vertical

def airtime(velocity_vertical,init_height,g=9.81):
    return ((velocity_vertical + math.sqrt(velocity_vertical**2 + 2*g*init_height))/g)

def throw_distance(angle,velocity,init_height=1.8):
    velocity_horizontal,velocity_vertical = velocity_decomposition(angle,velocity)
    ball_airtime=airtime(velocity_vertical,init_height)
    throw_distance = velocity_horizontal*ball_airtime
    return throw_distance
    
def throw_position(angle,velocity,time,init_height=1.8):
    velocity_horizontal,velocity_vertical = velocity_decomposition(angle,velocity)
    ball_airtime=airtime(velocity_vertical,init_height)

    if time < ball_airtime:
        return velocity_horizontal*time
    else:
        return throw_distance(angle,velocity,init_height)



total_throw_dist = throw_distance(angle,velocity,init_height)
total_throw_pos = throw_position(angle,velocity,1,init_height)
print(total_throw_dist)
print(total_throw_pos)



