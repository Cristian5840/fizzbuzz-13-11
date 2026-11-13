#/fizzbuzz/fizzbuzz.py
#/fizzbuzz/test_fizzbuzz.py




def fizzbuzz(num):
    if num%3==0:
     return "fizz"
    if num%5==0:
       return"buzz"
    if num%3==0 and num%5==0:
       return "fizzbuzz"
    return num

    test_fizzbuzz.py
    import unittest
from fizzbuzz import fizzbuzz
class Testfizzbuzz(unittest.TestCase):