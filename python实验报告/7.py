#  编写程序，实现根据用户输入的数字n，
#  输出斐波那锲数列前n项的

fib = lambda n: n if n<2 else fib(n-1) + fib(n-2)



# n = int(input(""))
#
#
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# for i in range(1, n + 1):
#     print(fib(i))
