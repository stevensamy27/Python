# --------------------
# -- Debugging Code --
# --------------------

my_list = [1, 2, 3]

my_dictionary = {"Name": "Stiiv", "Age": 36, "Country": "Egypt"}

for num in my_list:

  print(num)

for key, value in my_dictionary.items():

  print(f"{key} => {value}")

def function_one_one():

  print("Hello From Function One")

function_one_one()


### EXPLATION ###
'''
1- we must Select or Determine a BreakPoint that we need to chech
2- Run the code as Run And Debugging (Ctrl+Shift+D) 
3- if we change on the code we can reload a debugging
'''

### OUTPUT ###
'''
1
2
3
Name => Stiiv
Age => 36
Country => Egypt
Hello From Function One

'''