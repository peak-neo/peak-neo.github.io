def create():
    import time
    import os

    # title = input("标题: ")
    title = "winxray"
    t = time.strftime("%Y-%m-%d",time.localtime())
    filename = t + "-" + title + ".md"
    print(filename)
    '''创建新博客文件'''
    if not os.path.exists(filename):
        f = open("./_posts/drafts/" + filename,"w")
        f.close()
        print(filename + " created")
    else:
        print(filename + " already existed.")
    return

create()
