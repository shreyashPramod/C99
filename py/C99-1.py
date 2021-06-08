f=open("D:/python/C98/test.txt")
fileLines=f.readlines()
for line in fileLines:
    print(line)

introString="My name is shreyash, my age is 14"
words=introString.split(",")
print(words)

def greet(name):
    print("Hello,"+name+".How are you?")

greet("Shreyash")


