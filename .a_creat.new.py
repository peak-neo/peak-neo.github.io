import time
import os

# def create():

#     title = input("标题(尽量使用字母而非汉字或其它字符): ")
#     ftitleList = title.split()
#     ftitle = ""
#     for i in range(0,len(ftitleList)):
#         temp = ftitleList[i]
#         if i != (len(ftitleList) - 1):
#             ftitle = ftitle + temp + "-" 
#         else:
#             ftitle = ftitle + temp
#     t = time.strftime("%Y-%m-%d",time.localtime())
#     filename = t + "-" + ftitle + ".md"
    
#     '''创建新博客文件'''
#     if not os.path.exists(filename):
#         f = open("./_posts/drafts/" + filename,'w')
#         print(filename)
#         f.close()
#         print(filename + " created")
#     else:
#         print(filename + " already existed.")
#     return

# create()

title = input("标题(尽量使用字母而非汉字或其它字符): ")
ftitleList = title.split()
ftitle = ""
for i in range(0,len(ftitleList)):
    temp = ftitleList[i]
    if i != (len(ftitleList) - 1):
        ftitle = ftitle + temp + "-" 
    else:
        ftitle = ftitle + temp
t = time.strftime("%Y-%m-%d",time.localtime())
filename = t + "-" + ftitle + ".md"
head = f'''
---
    layout: article
    sharing: true
    date: {t}
    title: {ftitle}
    author: Neolux Lee
    tags: Unclassified
---
'''
with open(f"_posts/drafts/{filename}","a") as f:
    f.write(head)
    f.close()
# os.system(f"echo {head} >> /_posts/drafts/{filename}")
