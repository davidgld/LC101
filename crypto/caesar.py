from helpers import alphabet_position, rotate_character
  

def encrypt(text, rot):
  encrypted_str = ''
  for i in range(len(text)):
    encrypted_str += rotate_character(text[i], rot)
  return encrypted_str
print(encrypt("pYthon", 26))
