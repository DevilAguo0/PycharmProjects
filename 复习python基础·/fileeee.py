with open("/Users/wevilaguo/Desktop/azure-session-settings.txt","w") as filter:

    filter.write("www.google.com")
with open("/Users/wevilaguo/Desktop/azure-session-settings.txt","r") as filter:

    file = filter.read()
print(file)
