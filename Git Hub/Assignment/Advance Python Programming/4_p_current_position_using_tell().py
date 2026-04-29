file = open("myfile.txt","r")

print("Cursor Position At Start:",file.tell())

file.read(5)
print("Cursor position after reading 5 characters:", file.tell())

file.close()