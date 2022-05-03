import sys

shift_num = int(sys.argv[1])
uppercase_message = ""
for line in sys.stdin:
    uppercase_message += line.upper()

  
block = 0 #keeps track of 5 letters per block
per_line = 0 #keepts track of 10 blocks per line
encrypted = ""


for char in uppercase_message:
  asc = ord(char) #to find the value in ascii of the character so we can encrypt
  if (asc >= 65 and asc <= 90):
    is_letter = True #do this to make sure we aren't changing the character of any spaces/specia    l characters
  else:
    is_letter = False
  if not(is_letter):
    continue
  else:
    block += 1
    new_char = chr((asc + shift_num-65) % 26 + 65)
    if block == 5:
      per_line += 1
      if per_line == 10:
        encrypted = encrypted + new_char + "\n"
        per_line = 0 #resets the var
        block = 0
      else:
        encrypted = encrypted + new_char + " "
        block = 0 #resets the var
    else:
      encrypted += new_char

print(encrypted)
     

