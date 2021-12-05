# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))
print(sum(a, 40))

# round(number, numofdigits)
print(round(150.500))
print(round(150.501))

print(round(150.554, 2))
print(round(150.555, 2))

# range(start, end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ") # sep = to switch the Defult Separator (space) to (|) 

print("First Line", end=" ")# to switch the default end ( /n ) to (space)
print("Second Line")
print("Third Line")


# # # OUTPUT # # # 
''' 
# sum()
70
110


# round()
150
151
150.55
150.56


# range()
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# print()
Hello @ Osama @ How @ Are @ You
Hello | Osama | How | Are | You
First Line Second Line
Third Line         

'''