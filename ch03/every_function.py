program_language=['c','cpp','python','java','go']
print("My first program language is "+program_language[0])
print("The language i want to learn is  "+program_language[-1])
print("The language list is "+str(program_language))

#change the go to golang to easy understand
program_language[-1]='golang'

#maybe cshapr is good
program_language.append('csharp')

#vb
program_language.insert(0,'vb')

#i dont like java
del program_language[4]

#csharp is hard so del it
print(program_language.pop()+'is hard so del it')

#cpp is hard too del
print(program_language.pop(2)+'is hard too so del')

#c is easy del
program_language.remove('c')

print(program_language)

program_language.sort()

print(program_language)

print("Now i have "+str(len(program_language))+" languages")
