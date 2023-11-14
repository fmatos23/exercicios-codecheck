
# Given the x- and y-coordinates of a point, print the quadrant plane in which the point sits, either 
# "First", "Second", "Third", "Fourth". If it lies on an axis, print the name of the axis: "X-axis" or
# "Y-axis". If it is the origin point, print "Origin".

point = [0, 0]
x = point[0]
y = point[1]

if point == [0,0]:
   print("Origin")
   
elif x == 0:
   print('Y-axis')
   
elif y == 0:
   print('X-axis')
   
elif x > 0 and y > 0:
   print('First')
elif x < 0 and y > 0:
   print('Second')
elif x < 0 and y < 0:
   print('Third')
elif x > 0 and y < 0:
   print("Fourth")
  
