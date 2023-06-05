import yagmail
yag = yagmail.SMTP(user='clarenceguo2060@gmail.com', password='nxizxpihjgshyqfs', host='smtp.gmail.com', port='465')
# yag.send('clarenceguo5@gmail.com', 'subject', 'body')
contents = ['Hello', 'World', 'This is a test','/Users/wevilaguo/PycharmProjects/pythonOfficeLearn/yagmailtext.py','/Users/wevilaguo/Desktop/gamesite.png']
yag.send('clarenceguo5@gmail.com', subject = "I now can send an attachment",contents=contents)

print('finished')


