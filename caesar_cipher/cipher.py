'''
Required Features: 
- [ ] Create an encrypt function that takes in a plain text phrase and a numeric shift.
- [ ] the phrase will then be shifted that many letters.
- [ ] shifts that exceed 26 should wrap around
- [ ] shifts that push a letter out or range should wrap around

- [ ] Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

- [ ] Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- [ ] Devise a method for the computer to determine if code was broken with minimal human guidance.
'''

def char_to_number(char):
  return ord(char)

def number_to_char(number):
  return chr(number)


def encrypt(text_to_encrypt, shift):
  '''
  Input: Takes in a string of text to encrypt and an integer for the number of positions to shift during encryption.
  Output: Encrypted message as a string.
  '''
  
  encrypted_message = ""
  
  for char in text_to_encrypt:
    #could use regex to find if it is a character.  If it is not, skip and leave unchanged.
    #if char in a-z or A-Z

    plain_number = char_to_number(char)
    shifted_number = plain_number + shift
    encrypted_letter = number_to_char(shifted_number)

    encrypted_message += encrypted_letter

  return encrypted_message


def decrypt(text_to_decrypt, shift):
  '''
  Input: Takes in a string of text to decrypt and an integer for the number of positions to shift during decryption.
  Output: Decrypted message as a string.
  '''
  pass


def crack(text_to_decrypt):
  '''
  Input: Takes in a string of text to decrypt.
  Output: Decrypted message as a string.
  '''
  pass
