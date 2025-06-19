# fileabc = open('regexdata.txt','w+')
# fileabc.write('Using w+ mode in file handling')
# print(fileabc.read(500))
# fileabc.close()
#
# fileabc = open('regexdata.txt','a+')
# fileabc.write("Using a+ mode in file handling")
# print(fileabc.read(100))
# fileabc.close()
#
# fileabc = open('regexdata.txt','r+')
# fileabc.write("Using r+ mode in file handling")
# print(fileabc.read(100))
# print(fileabc.tell()) # Tells the cursor position
# fileabc.seek(0) # Changes the position of cursor to specified position
# print(fileabc.read(100))
# fileabc.close()

# New syntax
# with open('regexdata.txt','r')as f:
#     print("Below is New Suntax Output ->")
#     print(f.read())
#     # No close is required


# with open('regexdata.txt','r')as f:
#     print("Below is New Syntax Output ->")
#     print(f.readline()) # reads one line at a time
#     print(f.readline())
#     print(f.readline())
#
# print("Using Loop: ")
# with open('regexdata.txt','r') as f:
#     for i in f:
#         print(i)
#
# with open('regexdata.txt','r') as f:
#     print(f.readlines()) # Reads the file in form of list where each line is an element

# with open("regexdata.txt",'r') as f:
#     for i in f.readlines():
#         for j in i.split():
#             print(j)
import csv
f = open('regexdata.txt')
csv_f = csv.reader(f)
for i in csv_f:
    print(i)
