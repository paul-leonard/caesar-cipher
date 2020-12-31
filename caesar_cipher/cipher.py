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

# from corpus_loader import word_list
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
  possible_plain_messages = []
  for i in range(6):
    possible_plain_messages.append(decrypt(text_to_decrypt, i))

    # count the total "words" in this plain_message
    candidate_words = possible_plain_messages[i].split()
    total_words = len(candidate_words)
    total_real_words = 0

    for candidate in candidate_words:
      potential_word = re.sub(r'[^A-Za-z]+', '', candidate)

      # determine if each word is an english word
      # if potential_word is in corpus:
      #  total_real_words += 1

    # calculate the english-word-percentage of each plain_message
    score = total_real_words / total_words

    # figure out the best data structure to store these 26 (phrases, scores) in

    print("************************************************")
    print(f"*** possible plain message with a shift of {i} ***")
    print(possible_plain_messages[i])
    print("total_words: ", total_words)
    print("total_real_words: ", total_real_words)
    print("score: ", score)
    print("************************************************")

  # find max score and return the associated phrase



if __name__ == '__main__':
  crack(encrypt("hello there! *captain* planet!",4))