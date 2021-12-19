# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

myBirthday = datetime.datetime(1982, 10, 25)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print("#"*50)

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))




#####OUTPUT#####
'''
1982-10-25 00:00:00
Mon
Monday
Oct
October

##################################################

25 October 1982
25, October, 1982
25/October/1982
25 - October - 1982
October - 1982

'''