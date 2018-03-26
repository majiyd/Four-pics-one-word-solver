import string
sourceFile = open('words.txt', 'r')
bigStringFile = open('bigString.txt', 'w')
dataDump = sourceFile.readlines()
initialString = '/'
for data in dataDump:
    initialString+=(data.strip()+'/')
    initialString.strip()

bigStringFile.write(initialString)



