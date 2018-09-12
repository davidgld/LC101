def alphabet_position(letter):
  
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    letter = letter.upper()
    
    for i in range(0, len(alphabet)):
        if alphabet[i] == letter:
          return i
          

def rotate_character(char, rot):

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if char not in alphabet and char not in alphabet2:
    return char
  
  letter_index = alphabet_position(char) + rot
  letter_index = letter_index % 26 
  
 
  if char.isupper():
        start = ord('A')
  elif char.islower():
        start = ord('a')
  else:
        return char

  c = ord(char) - start
  i = (c + rot) % 26 + start
  return chr(i)

  