# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"] # just a skill 

mySkillsWithCounter = enumerate(mySkills, 20) # Skill + Counter start from 20

print(type(mySkillsWithCounter))

for x, y in mySkillsWithCounter:

  print(f"{x} - {y}") # ( Counter - skill )
 
print("#" * 50)

# help() 

print(help(sum))

print("#" * 50)

# reversed(iterable)

myString = "Elzero"

print(reversed(myString))

for letter in reversed(myString):

  print(letter)

for s in reversed(mySkills):

  print(s)




###OUTPUT###

# enumerate(iterable, start=0)
  '''
<class 'enumerate'>
20 - Html
21 - Css
22 - Js
23 - PHP
##################################################
  '''


# help() 
  '''
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
  Return the sum of a 'start' value (default: 0) plus an iterable of numbers

  When the iterable is empty, return the start value.
  This function is intended specifically for use with numeric values and may
  reject non-numeric types.

None
  '''


# reversed(iterable)
'''
<reversed object at 0x000001C55969F220> ##### pecouse just one Eliment exist
o
r
e
z
l
E
PHP
Js
Css
Html

'''