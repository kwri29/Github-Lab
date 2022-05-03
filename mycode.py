import sys
for line in sys.stdin:
    line = line.upper()
def mycipher(shift_num, txt):
  block = 0 #keeps track of 5 letters per block
  per_line = 0 #keepts track of 10 blocks per line
  encrypted = ""

  for char in txt:
    num1 = shift       
    asc = ord(char) #to find the value in ascii of the character so we can encrypt
    if (asc >= 65 and asc <= 90):
      is_letter = True #do this to make sure we aren't changing the character of any spaces/specia    l characters
    else:
      is_letter = False
    if not(is_letter):
      continue
    else:
      block += 1
      while num1 > 0:
        asc+=1
        num1-=1
        if asc > 90:
          asc = 65 + num1 #to make sure we stay in the range of A-Z
          num1 = 0
      if block == 5:
        if per_line == 10:
          encrypted = encrypted + chr(asc) + "\n"
          per_line = 0 #resets the var
        else:
          encrypted = encrypted + chr(asc) + " "
          block = 0 #resets the var
      
     

