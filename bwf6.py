
# Given three numbers x, y, z, print "Distinct" if they are all distinct,
# "Two" if two are the same, or "All" if all three are the same.

x = 0 
y = 0 
z = 0 
if x == y and y == z:
   print('All')
elif x != y and x != z and y!= x and y != z and z!= x and z != y:
   print("Distinct")
elif x == y and x != z or y == x and y != z or z == x and z != y or y == z and y != x:
   print("Two")


