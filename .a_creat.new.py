import time
import os

def create():


    title = input("标题(尽量使用字母而非汉字或其它字符): ")
    ftitleList = title.split()
    ftitle = ""
    print(ftitleList)
    # for i in (0,(len(ftitleList)-1)):
    #     temp = ftitleList[i]
    #     if i != (len(ftitleList) - 1):
    #         ftitle = ftitle + temp + "-" 
    #     else:
    #         ftitle = ftitle + temp
    # t = time.strftime("%Y-%m-%d",time.localtime())
    # filename = t + "-" + ftitle + ".md"
    # print(filename)
    # '''创建新博客文件'''
    # if not os.path.exists(filename):
    #     f = open("./_posts/drafts/" + filename,"w")
    #     f.close()
    #     print(filename + " created")
    # else:
    #     print(filename + " already existed.")
    # return

create()

os.system(".a_update_blog.bat")
