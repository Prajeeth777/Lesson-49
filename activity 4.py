firstfile=input("Enter the name of first file")
secondfile=input("Enter the name of second file")

f1=open(firstfile,'r')
f2=open(secondfile,'r')

print("File 1 before appending content \n",f1.read())
print("File 2 before appending content \n",f2.read())

f1.close()
f2.close()

f1=open(firstfile,'r')
f2=open(secondfile,'a')

f2.write(f1.read())

f1.seek(0)
f2.seek(0)

f1.close()
f2.close()
