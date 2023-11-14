# On a chessboard, positions are marked with letters between a and h for the column and a
# number between 1 and 8 for the row. 

# Give a 2 character input string with a letter (a-h) and a number (1-8), print "Corner" if the 
# value indicates a square on a corner. Print "Border" if the value indicates a square on an 
# edge of the board. Otherwise, print "Inside".
inputStr = 'a1' 
if inputStr == 'a1' or inputStr == 'a8' or inputStr == 'h8' or inputStr == 'h1':
   print("Corner")

elif 'a' in inputStr or 'h' in inputStr or '8' in inputStr or '1' in inputStr:
   print("Border")
   
else:
   print("Inside")
