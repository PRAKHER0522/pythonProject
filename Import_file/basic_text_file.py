filename = 'C://Users//win-10//Desktop//moby_dick.txt'
file = open(filename, mode ='r') #r is used for read
print(file.readline())
print(file.readline())
print(file.readline())
text= file.read()
#with open('C://Users//win-10//Desktop//moby_dick.txt') as file:
#read line from file
#1st line
   #print(file.readline())
#second line
   #print(file.readline())
#third line
   #print(file.readline())
file.close()