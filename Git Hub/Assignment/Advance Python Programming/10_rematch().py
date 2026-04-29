import re

text=input("Enter A String:")

word=input("Enter Word To Match:")

result=re.match(word,text)

if result:
    print("Word matched at the beginning of the string")
else:
    print("Word not matched")