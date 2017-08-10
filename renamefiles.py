import os

def renaming():
    f_list=os.listdir(r"C:\Users\prasa\Downloads\prank")
    print(f_list)
    pwd=os.getcwd()
    os.chdir(r"C:\Users\prasa\Downloads\prank")
    print(pwd)
    for f in f_list:
        os.renames(f,f.translate("0123456789"))
    os.chdir(pwd)
renaming()
