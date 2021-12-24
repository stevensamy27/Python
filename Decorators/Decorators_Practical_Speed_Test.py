# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time

def speedTest(func):

  def wrapper():

    start = time()

    func()

    end = time()

    print(f"Function Running Time Is: {end - start}")

  return wrapper

@speedTest
def bigLoop():

  for number in range(1, 20):

    print(number)

bigLoop()