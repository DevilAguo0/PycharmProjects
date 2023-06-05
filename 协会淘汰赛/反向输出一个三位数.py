n = int(input(""))
a = n // 100
b = (n - a * 100) // 10
c = n % 10
n = a + b * 10 + c*100
print(n)

n = input('')
print(n[::-1])

