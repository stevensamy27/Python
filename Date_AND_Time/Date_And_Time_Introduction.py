# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

print("#" * 40)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)

# Print Specific Date
print(datetime.datetime(1982, 10, 25))
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

print("#" * 40)

myBirthDay = datetime.datetime(1982, 10, 25)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")



# Print The Current Date and Time
'''
2021-12-18 02:07:43.654034
########################################
'''

# Print The Current Year
'''
2021
'''

# Print The Current Month
'''
12
'''

# Print The Current Day
'''
18
########################################
'''

# Print Start and End Of Date
'''
0001-01-01 00:00:00
9999-12-31 23:59:59.999999
########################################
'''

# Print The Current Time
'''
02:07:43.663858
########################################
''' 

# Print The Current Time Hour
'''
2
'''

# Print The Current Time Minute
'''
7
'''

# Print The Current Time Second
'''
43
########################################
'''

# Print Start and End Of Time
'''
00:00:00
23:59:59.999999
########################################
'''

# Print Specific Date
'''
1982-10-25 00:00:00
1982-10-25 10:45:55.150364
########################################

My Birthday is 1982-10-25 00:00:00 And Date Now Is 2021-12-18 02:07:43.682114
 I Lived For 14299 days, 2:07:43.682114
 I Lived For 14299 Days.
'''
    