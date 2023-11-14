
# Given an input string, when the first and last letters are equal, 
# print the string with the first and last letters removed. 
# Otherwise, print the original string.

inputStr = 'test'
newStr = ''
if len(inputStr) == 1:
   print(inputStr)
elif inputStr[0] == inputStr[-1]:
   newStr = inputStr[1:-1]
   print(newStr)
  
else:
   print(inputStr)
