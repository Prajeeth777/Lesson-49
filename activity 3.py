file=open(WWW.txt","r")

content=file.read()
colist=content.split("\n")

for i in colist:
  if i:
    count+=1

file.close()
print("NUmber of lines in the file is ",count)
