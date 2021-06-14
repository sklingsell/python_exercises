import math

my_angle = float(input('Please enter the angle (in degrees): '))
my_velocity = float(input('Please enter the velocity (in km/h): '))
my_height = float(input('Please enter the throw height (in meters): '))

angle_radian = math.radians(my_angle)
print("The throw angle in radians: "+ str(angle_radian))

velocity_mps = my_velocity/3.6
print("The velocity in m/s is: " + str(velocity_mps))

velocity_horizontal = velocity_mps * math.cos(angle_radian)
print("The throw velocity in the horizontal direction is: " + str(round(velocity_horizontal,2)))

velocity_vertical = velocity_mps * math.sin(angle_radian)
print("The throw velocity in the vertical direction is: " + str(round(velocity_vertical,2)))

airtime = (velocity_vertical + math.sqrt(math.pow(velocity_vertical,2)+2*9.81*my_height))/9.81
print("The ball airtime is: " + str(round(airtime,2)))

throw_distance = velocity_horizontal*airtime
print("The throw distance is: " + str(round(throw_distance,2)))

