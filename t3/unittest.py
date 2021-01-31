import math

from math import sum, substact




def test_sum():
   assert sum(1,2) == 1
   assert sum(1.1, 2.1) == 4.3

def test_subtract():
   assert subtract(1,1) == 0
   assert subtract(2,1) == 1


if __name__ == '__main__':
   test_sum()
   test_subtract()



