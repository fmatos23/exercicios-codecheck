
# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. The first place on the board, a1, is black. The next
# is white, alternating across a row. Odd rows start with black, even rows start with white.

# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Black" or
# "White" indicating if the square is black or white.
def par(n):
   if n % 2 == 0:
      return True
      
def impar(n):
   if n % 2 != 0:
      return True
      
      
inputStr = 'a1' 

if par(int(inputStr[1])) and 'b' in inputStr or par(int(inputStr[1])) and 'd' in inputStr or par(int(inputStr[1])) and 'f' in inputStr or par(int(inputStr[1])) and 'h' in inputStr:
   print("Black")
elif impar(int(inputStr[1])) and 'b' in inputStr or impar(int(inputStr[1])) and 'd' in inputStr or impar(int(inputStr[1])) and 'f' in inputStr or impar(int(inputStr[1])) and 'h' in inputStr:
   print("White")
   
   
elif impar(int(inputStr[1])) and 'a' in inputStr or impar(int(inputStr[1])) and 'c' in inputStr or impar(int(inputStr[1])) and 'e' in inputStr or impar(int(inputStr[1])) and 'g' in inputStr:
   print("Black")
elif par(int(inputStr[1])) and 'a' in inputStr or par(int(inputStr[1])) and 'c' in inputStr or par(int(inputStr[1])) and 'e' in inputStr or par(int(inputStr[1])) and 'g' in inputStr:
   print("White")
   


