#1
'''
f = open("T19Entrada.txt","r")

str = f.readline()    
print(str)
    

f.close()


#2
with open("T19Entrada.txt", "r") as f:
    data = f.read()
    print(data.upper())  
  
#3
with open("T19Entrada.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))
'''

#4
with open("T19Entrada.txt", "r") as f:
    data = f.read()
    words=data.split()
    print(len(data))