import os
import shutil
#os.mkdir('newfolder')
os.getcwd()
path='D:/python'
isexist=os.path.exists(path)
print(isexist)
root_ext=os.path.splitext(path)
print("rootprt",root_ext[0])
print("extprt",root_ext[1],"\n")
print("before copying file")
print(os.listdir(path))
source="/python/C98.py"
destination="/python/C99-1.py"
dest=shutil.copy(source,destination)
print("after copying file")
print(os.listdir(path))
path1="D:/python/newfolder"
print("before moving file")
print(os.listdir(path1))
source1="D:/python/newfolder/mp4"
destination1="D:/python/newfolder/png"
dest1=shutil.move(source1,destination1)
print("after moving file")
print(os.listdir(path1))