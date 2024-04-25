name = input()
family = input()

print(name, family, sep="@@")

print(name, end="")
print(family)

#list:
my_list = range(10)
my = list(my_list)
print(my)
my.append(3)
my.insert(2, 9)
my.pop()
my.remove(3)
m = []
del my

#tuple

l = (1, 2)
print(l[1])

#set
s = set(range(5))
s.add(6)
print(s)

#dictionary

mydict = {"name":"ali", "family":"ahmadi","age":"21"}
mydict["country"]="iran"
print(mydict)
print(list(mydict.values()))

for k in mydict:
    print(k)#key
    print(mydict[k])#values

for i in mydict.items():
    print(i)

for k, v in mydict.items():
    print(k, v, sep="=")

#tamrin1
def multy():
    for i in range(1,11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()
multy()

#tamrin2
num = int(input("enter number:"))
list1 = []

for i in range(0, num):
    name = input("enter name:")
    mdict = dict()
    mdict["name"] = name
    list1.append(mdict)

print(list1)

#tamrin3
import os
n = int(input("enter number:"))
name = input("enter name:")
os.mkdir(name)
os.chdir(name)
for i in range(0, n):
    os.mkdir(str(i))

#file
#f = open("test.txt","w+")
#f.write("ali")
#f.close()

#tamrin4
name = input("enter name:")
os.mkdir(name)
os.chdir(name)
f = open("test.txt", "w+")
n = int(input("enter number:"))
for i in range(0, n):
    name = input("enter name:")
    f.write(name + " ")

f.close()



