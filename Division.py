from error import DivisionByZero
from Calculator import Calculator

class Division (Calculator):
  def compute(self,a, b):
    if b == 0:
      raise DivisionByZero("Attemp to divide by zero")
    else:
      return a / b

