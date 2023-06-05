# 2、编写程序，打开“Python之禅”文本文件，读出文件的全部内容，并判断：
# （1）该文本文件共有多少行？
# （2）该文件中以大写字母A开头的有多少行？
# （3）一行中包含字符最多的及包含字符最少的分别在第几行？
# （4）统计该文件中各个单词出现的次数。
"""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
# with open("python之禅", "r+") as p:
#     python_conment=p.read()
#     # print(python_conment)
#     # print(p.read())
#     k=1
#     for i in python_conment:
#         if i=="A":
#             k+=1
#     print(k)



# print(len(open("python之禅").readlines()))
num=[]
a=open("python之禅").readlines()
for i in a:
    k=len(i)
    num.append(k)
    result=max(num)
    result2=min(num)
num.sort()
print(num[1])
print(num[-1])
# print(result)
# print(result2)
