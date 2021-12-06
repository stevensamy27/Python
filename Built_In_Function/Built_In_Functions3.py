# ------------------------
# -- Built In Functions --
# ------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------

# abs()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#" * 50)

# pow(base, exp, mod) => Power
print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10

print("#" * 50)

# min(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))
print(min("X", "Z", "O"))
print(min(myNumbers))

print("#" * 50)

# max(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("X", "Z", "O"))
print(max(myNumbers))

print("#" * 50)

# slice(start, end, step)
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])


'''
# abs()
100
100
10.19
10.19

##################################################

pow()
32
2

##################################################

min()
-50
O
-100

##################################################

max()
30
Z
100

##################################################

slice()
['A', 'B', 'C', 'D', 'E']
['A', 'B', 'C', 'D', 'E']
['C', 'D', 'E']

'''