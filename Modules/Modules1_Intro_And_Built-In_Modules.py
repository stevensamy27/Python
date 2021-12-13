# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Lot Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random # here we call the module with all function 
print(random)
print ('#' * 50)
print(f"Print Random Float Number {random.random()}") # and here we must say witch function we need from the module
                          #Name_Of_Module.Name_Of_Function()

# Show All Functions Inside Module
print(dir(random))
print ('#' * 50)

# Import One Or Two Functions From Module
from random import randint, random # here we call just a specific function not all
print(f"Print Random Float {random()}") # so we mustnot say a name of the module, just a function
print(f"Print Random Integer {randint(100, 900)}") # randint >> randome integer



# Import Main Module
'''
<module 'random' from 'C:\\Users\\amr\\AppData\\Local\\Programs\\Python\\Python39\\lib\\random.py'>

##################################################
Print Random Float Number 0.4101695308204666
'''

# Show All Functions Inside Module
'''
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 
 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__',
 '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
 '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', 
 '_exp', '_floor', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', 
 '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 
 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'] 
'''

# Import One Or Two Functions From Module
'''
Print Random Float 0.15499380701357612
Print Random Integer 498

'''