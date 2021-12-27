# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

# number = int(input("Write Your Age: "))

# print(number)
# print(type(number))

try:  # Try The Code and Test Errors

  number = int(input("Write Your Age: "))

  print("Good, This Is Integer From Try")

except:  # Handle The Errors If It's Found

  print("Bad, This is Not Integer")

else:  # If Theres No Errors

  print("Good, This Is Integer From Else")

finally:

  print("Print From Finally Whatever Happens")

print(50*"#")
try:

  # print(10 / 0)
  # print(x)
  print(int("Hello"))

except ZeroDivisionError: # in case ZeroDivisionError  

  print("Cant Divide")

except NameError: # in case NameError

  print("Identifier Not Found")

except ValueError: # in case ValueError

  print("Value Error")

except:

  print("Error Happens")


  ###OUTPUT###


'''
Write Your Age: 20
Good, This Is Integer From Try
Good, This Is Integer From Else
Print From Finally Whatever Happens


##################################################


Value Error 

'''

