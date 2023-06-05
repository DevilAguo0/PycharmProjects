with open("demo.txt", "w+") as file:
    file.write("hello world!")
    file_r = file.read()
    print(file_r)
# with open("demo.txt","r+") as fi:
#     fil=fi.read()
#     fi.write("hhhhhh")
#     print(fil)
