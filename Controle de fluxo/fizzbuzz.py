
def main(FizzBuzz):

    for i in range(1,100):
        if FizzBuzz(i):
          print("FizzBuzz")
        elif i % 3 == 0:
         print("Fizz")
        elif i % 5 == 0:
          print("Buzz")
        else:
          print(i)
        
def FizzBuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return True
    else:
        return False
    
main(FizzBuzz)