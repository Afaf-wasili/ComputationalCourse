'''
variable = open(filename, mode)
File Mode	Description
'r'	Opens the file in read-only mode.
'rb'	Opens the file in binary and read-only mode.
'r+'	Opens the file in both read and write mode.
'w'	Opens the file in write mode. If the file already exists, all the contents will be overwritten. If the file doesn’t exist, then a new file will be created.
'wb+'	Opens the file in read, write and binary mode. If the file already exists, the contents will be overwritten. If the file doesn’t exist, then a new file will be created.
'a'	Opens the file in append mode. If the file doesn’t exist, then a new file will be created.
'a+'	Opens the file in append and read mode. If the file doesn’t exist, then it will create a new file.
'''

'''
#Writing Data to a Text File
outfile = open('oceans.txt', 'w')
#outfile = open("/Users/afafwasili/ComputationalMC/Tutorial/Python/Outputtxt/oceans.txt", "w")    
outfile.write('Atlantic\n')
outfile.write('Pacific\n')
outfile.write('Indian\n')
outfile.write('Arctic\n')
outfile.close() #closing .txt file

'''
'''
#Append Data to a File, adding element
outfile = open('oceans.txt', 'a') #'a' For Append
outfile.write('Southern\n')
outfile.close()
'''

'''
#Reading Data From a File
infile = open("oceans.txt", "r")
#data = infile.read()
#print(data)
print(infile.read())
infile.close()
'''

'''
#Reading Data From a File with specific element

                     
infile = open('oceans.txt', 'r')
data = infile.read()
print(data)
infile.close()

'''
'''

#Reading File Using readline(), line by line with extra space b/w elements
infile = open('oceans.txt', 'r')
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
print(line1)
print(line2)
print(line3)
infile.close()
'''

'''

#Reading File Using readline(), line by line with lessspace b/w elements             
infile = open('oceans.txt', 'r')
line1 = infile.readline().rstrip('\n')
line2 = infile.readline().rstrip('\n')
line3 = infile.readline().rstrip('\n')
print(line1)
print(line2)
print(line3)
infile.close()

'''


#for Loop to Read All Lines from the file
file = open('oceans.txt', 'r')

for i in file:
    i = i.rstrip()
    print(i)

file.close()
