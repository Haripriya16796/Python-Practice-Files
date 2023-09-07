# Run the script by uncommenting each section

# print('Hello World')
# print(1+2)

# Create example.txt file in the same folder where this file is present

# file = open('example.txt','r')#read mode r is used to read the file
# content = file.read()
# print(content)
# file.close()# close it to stop the file from running
#
# file1 = open('example.txt','w')# write mode w 'rewrites' the whole content to new written content
# file1.write('My third line')
# print('Done')
# file.close()
#
# file1 = open('example.txt','a')# write mode a 'appends' the new content
# file1.write('\nMy third line')# \n is used to append in the next line
# print('Done')
# file.close()

file = open('example.txt','r')#read mode r is used to read the file
content = file.readlines()# reads in a list format
print(content)
print(len(content))

# file.delete


