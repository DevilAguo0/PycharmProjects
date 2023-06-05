# Split Multi Lines String
string = "Data \n is encrpted \n by Python"
print(string)
# Output
# Data
# is encrpted
# by Python
splited = string.split("\n")
print(splited) # ['Data ', ' is encrpted ', ' by Python']