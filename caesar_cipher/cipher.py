'''
Required Features: 
- [x] Create an encrypt function that takes in a plain text phrase and a numeric shift.
- [x] the phrase will then be shifted that many letters.
- [x] shifts that exceed 26 should wrap around
- [x] shifts that push a letter out or range should wrap around

- [x] Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

- [ ] Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- [ ] Devise a method for the computer to determine if code was broken with minimal human guidance.
'''

from caesar_cipher.corpus_loader import corpus_word_list
from caesar_cipher.corpus_loader import corpus_name_list
import re

def encrypt(text_to_encrypt, shift):
  '''
  Input: Takes in a string of text to encrypt and an integer for the number of positions to shift during encryption.
  Output: Encrypted message as a string.
  '''
  
  encrypted_message = ""
  
  for char in text_to_encrypt:

    plain_number = ord(char)
    shifted_number = (plain_number + shift)

    # get lowercase characters back within the appropriate range 
    # decimal representation for a-z is 97-122 inclusive on both ends
    if plain_number >=97 and plain_number <= 122:
      while shifted_number > 122:
        shifted_number -= 26
      while shifted_number < 97:
        shifted_number += 26

    # get uppercase characters back within the appropriate range 
    # decimal representation for A-Z is 65-90 inclusive on both ends
    elif plain_number >=65 and plain_number <= 90:
      while shifted_number > 90:
        shifted_number -= 26
      while shifted_number < 65:
        shifted_number += 26

    # shift a-z and A-Z, leave everything else alone and pass it through
    if (plain_number >=97 and plain_number <= 122) or (plain_number >=65 and plain_number <= 90):
      encrypted_letter = chr(shifted_number)
    else:
      encrypted_letter = char

    encrypted_message += encrypted_letter

  return encrypted_message


def decrypt(text_to_decrypt, shift):
  '''
  Input: Takes in a string of text to decrypt and an integer for the number of positions to shift during decryption.
  Output: Decrypted message as a string.
  '''
  return encrypt(text_to_decrypt, -shift)


def crack(text_to_decrypt):
  '''
  Input: Takes in a string of text to decrypt.
  Output: Decrypted message as a string.
  '''

  # run through all possible shifts, including the current one
  possible_plain_message = "nothing was input to decode"
  best_score = 0
  best_message = ""

  for shift_int in range(26):
    possible_plain_message = decrypt(text_to_decrypt, shift_int)

    # count the total "words" in this plain_message
    punctuated_potential_words = possible_plain_message.split()
    total_words = len(punctuated_potential_words)
    total_real_words = 0

    for punctuated_potential_word in punctuated_potential_words:
      this_potential_word = re.sub(r'[^A-Za-z]+', '', punctuated_potential_word)

      # determine if each word is an english word
      if this_potential_word.lower() in corpus_word_list:
       total_real_words += 1

      # determine if each word is a name
      if this_potential_word in corpus_name_list:
       total_real_words += 1

    # calculate the english-word-percentage of each plain_message
    score = total_real_words / total_words

    # figure out the best data structure to store these 26 (phrases, scores) in
    # find max score and return the associated phrase
    # or just figure out the max and the phrase and update it each time we loop through
    # only have to really store one... which is the best one... saves on memory space too

    if score > best_score and score > 0.6:
      best_score = score
      best_message = possible_plain_message

    print("*"*20)
    print(f"*** possible plain message with a shift of {shift_int} ***")
    print(possible_plain_message)
    print("total_words: ", total_words)
    print("total_real_words: ", total_real_words)
    print("score: ", score)
    print("*"*20)


  print("*"*20)
  print(f"Best score was {best_score} with the message being:")
  print(best_message)
  print("*"*20)

  return best_message



if __name__ == '__main__':
  crack(encrypt("Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd.",10))