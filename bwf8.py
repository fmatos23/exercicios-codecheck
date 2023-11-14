# Given three integers x, y, z, print the sum of the odd integers.

x = 2
y = 1
z = 3

lst = []
lst.append(x)
lst.append(y)
lst.append(z)
sum = 0
for c in lst:
    if c % 2 != 0:
        sum += c

print(sum)