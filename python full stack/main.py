#with open("hello.txt","w")as file:
#    file.write("hello,world\n")
#    file.write('this is another line in the file.\n')
#with open("hello.txt","r")as file:
#    a=file.read()
#    print(a)

#f=open("demofile.txt","r")
#print(f.read())

#with open("hello.txt","a")as file:
# file.write("next.file")


data=data2=""

with open('note.txt') as fp:
    data = fp.read()
with open('note1.txt') as fp:
    data2 = fp.read()

data += "\n"
data += data2

with open('note2.txt','w') as fp:
    fp.write(data)



