f=open("writefile.txt","r+")
print(f.read())
f.seek(4)
f.write("xyz")
f.seek(0)
print(f.read())
f.close()