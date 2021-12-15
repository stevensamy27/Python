# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------


# Directions
import sys
sys.path.append(r" D:\ccna") #jus add a new direction to read with system 
print(sys.path)

#Show Directions 
import module_sivo
print(dir(module_sivo)) # to show our functions on this module 
print("#" * 50) 

#Use Functions 
module_sivo.sayHello("Ahmed")
module_sivo.sayHello("Osama")
module_sivo.sayHello("Mohamed")

print("#" * 50) 

module_sivo.sayHowAreYou("Ahmed")
module_sivo.sayHowAreYou("Osama")
module_sivo.sayHowAreYou("Mohamed")

print("#" * 50) 

# Alias
# Replace THname of module
import module_sivo as ee  # to replace the name of this function as another name  and use it 

ee.sayHello("Ahmed")
ee.sayHello("Osama")
ee.sayHello("Mohamed")

print("#" * 50) 

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Osama")
ee.sayHowAreYou("Mohamed")

print("#" * 50) 

#To Call a Specific Function
from module_sivo import sayHello

sayHello("Osama")
 
#To Call a Specific Function  And Replace The name of Function
from module_sivo import sayHello as ss 

ss("Osama")

#######----OUTPUT---########

# Show Directions 
'''
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sayHello', 'sayHowAreYou']
'''


#Use Functions 
'''
Hello Ahmed
Hello Osama
Hello Mohamed
##################################################
How Are You Ahmed ?
How Are You Osama ?
How Are You Mohamed ?
##################################################
'''


# Alias
# Replace THname of module
'''
Hello Ahmed
Hello Osama
Hello Mohamed
##################################################
How Are You Ahmed ?
How Are You Osama ?
How Are You Mohamed ?
##################################################
'''

#To Call a Specific Function


'''
Hello Osama
Hello Osama
'''
