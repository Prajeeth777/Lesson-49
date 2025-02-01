file1=open("WWW.txt","r")
print("File in read mode\n")
print(file1.read())
file1.close()

file2=open("WWW.txt","w")
print("File in write mode....")
file2.write("Hi I am Prajeeth Kumar and I am 15 years old")
file2.close()

file3=open("WWW.txt","a")
print("File in append mode....")
file3.write("\nI am Prajeeth Kumar and I am 15 years old")
file3.close()
