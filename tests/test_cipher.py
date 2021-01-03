'''
Required Testing Features:
- [x] encrypt a string with a given shift
- [x] decrypt a previously encrypted string with the same shift
- [x] encryption should handle upper and lower case letters
- [x] encryption should allow non-alpha characters but ignore them, including white space
- [x] decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
- [x] refer to supplied unit tests.
'''

import pytest

from caesar_cipher import __version__
from caesar_cipher.cipher import encrypt, decrypt, crack


def test_version():
    assert __version__ == '0.1.0'


# additional tests
def test_decrypt_shift_20():
    actual = decrypt(encrypt("apple", 20),20)
    expected = "apple"
    assert actual == expected


def test_encrypt_very_large_shift():
    actual = encrypt("apple", 101)
    expected = "xmmib"
    assert actual == expected


def test_encrypt_negative_wrapping():
    actual = encrypt("apple", -3)
    expected = "xmmib"
    assert actual == expected



# supplied tests
def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected


def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected


def test_encrypt_shift_20():
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected


def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected


def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected


def test_with_non_alpha():
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected


def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected


def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected


def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = ""
    assert actual == expected