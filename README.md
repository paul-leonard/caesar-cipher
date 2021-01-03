# caesar-cipher
A starter project in cryptography, this repo contains functions to encrypt, decrypt, and crack messages using the Caesar Cipher.

## Lab Submission Pull Requests
[Lab38: Cryptography](https://github.com/paul-leonard/caesar-cipher/pull/1)

## Release Info
**Author**: Paul Leonard
**Version**: 1.0.0

## Overview
The Caesar Cipher is a very basic encryption method which was effective in historic times, but today is so simple that it is only useful as a "hello world" exercise in cryptography.  To encrypt a message using this method, each letter is shifted by a given amount of positions to another letter.  For example, the letter "a" would be shifted to "c", for a given shift of 2.  Then to decrypt the message, the recipient would shift the letters back by -2, or two to the left.  This module encrypts, decrypts, and cracks messages using the Caesar cipher.

## Architecture
To encrypt messages, the function takes in the plain text to encode and the desired shift.  The algorithm then obtains the integer value for the given unicode character and adds the shifted value.  If the shifted value, positive or negative, takes the value outside of the range for given latin characters, the value is adjusted to correct it for wrapping.  The ranges are seperate for lower and upper case characters.  The number is then converted back into the unicode character and reassembled into an encrypted message.  To decrypt messages, the encrypt function is called with the equal and opposite shift.  This returns the decoded message.

For cracking messages that are encoded using the Caesar Cipher, the algorithm performs a decrypting shift on all 26 possible shifts.  Each of those decodings are then evaluated to determine if the "decrypted" message contains English words and names.  This is done by determining if the words are in a word and name corpus imporoted from the Natural Language Toolki (nltk).  Each message is evaluated to determine its known words+names ratio to total words.  If a message is found that contains content of at least 60% known words, then the phrase with the highest percentage is returned.

## Change Log
**0.9.0** 12-30-2020 - Initial beta release
**1.0.0** 1-2-2020 - Initial release

## Credits and Collaborations
- [unicode values](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
- Taylor's suggestion of ord()
- [ord()](https://www.geeksforgeeks.org/ord-function-python/)
- [chr()](https://stackoverflow.com/questions/29818519/what-is-the-opposite-of-pythons-ord-function#:~:text=For%20example%2C%20chr(97),i%20is%20outside%20that%20range.)
- [Print lists in Python (4 Different Ways)](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/)
- [f string](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python)
