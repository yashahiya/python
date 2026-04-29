import re

text=input("Enter A String:")

word=input("Enter Word To Search:")

result=re.search(word,text)

if result:
    print("Word found at position:",result.start())
else:
    print("Word Not Found.")