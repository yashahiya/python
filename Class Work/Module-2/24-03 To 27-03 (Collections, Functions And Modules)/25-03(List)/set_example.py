myset={'a','b','c','d','a'}

#print(myset)
#print(len(myset))

"""if "b" in myset :
    print("yes...")
else :
    print("no....")"""

print(myset)

#myset.add('g') #for add
#myset.update(['k','l','m','n']) #update or add 
#myset.remove('d') #remove value
#myset.pop() #delete first value
#myset.clear() #clear all value
#del myset #for delete
#print(myset)

newset={'a','l','m','n'}
print(newset)
#x=myset.union(newset) #merge
x=myset.intersection(newset) #only matching value
print(x)