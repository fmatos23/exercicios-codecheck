# Given three input strings, print all but the shortest one, in the order given,
# separated by a space. If all three string lengths are equal, print "All Equal".

s1 = 'hi'
s2 = 'hello'
s3 = 'morning'


def maxi(s1, s2):
    if len(s1) > len(s2):
      return s1
    else:
      return s2


def maxi2(s1, s2, s3):
    if len(s3) > len(maxi(s1, s2)):
        return s3
    return maxi(s1, s2)


if len(s1) == len(s2) == len(s3):
    print("All Equal")

else:
    print(maxi(s1, s2) + ' ' + maxi2(s1, s2, s3))
