import random
def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='    ')
        print()

m = 4 
n = 2 

a = []
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(10, 20))

b = []
for i in range(n):
    b.append(sum(a[i]))  

print("A massivi:")
printList(a)
print("\nB massivi:")
print(b)
