#python 2
import itertools as itt
import string, re

print('''
    Welcome to my Four pics one word helper!!!
    This script computes all the possible word permutations using the letters and available spaces
    Just enter the letters provided and the number of spaces.
''')
test_string = raw_input('Kindly input all the letters available including repetitions: \n').strip()
number_of_spaces = int(raw_input('Input the number of available of spaces: '))
result = itt.permutations(test_string, number_of_spaces)


bigString = open('bigString.txt','r')
dictString = bigString.readline()
for res in result:
    res = list(res)
    test_case = (string.joinfields(map(str, res), ''))
    test_case = '/'+test_case+'/'
    if (test_case in dictString):
        print test_case
    # pattern = re.compile(test_case, re.IGNORECASE)
    # isMatch = pattern.search(dictString)
    # if isMatch:
    #     print(test_case)
