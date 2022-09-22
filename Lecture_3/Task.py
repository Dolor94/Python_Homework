def f(x):
    return x**2

g = f  
print((f(4)))
print((g(4)))



def sum(x, y):
    return x+y 
sum = lambda x, y: x+y

def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    
calc(mylt, 4, 5)
calc(sum, 4, 5)
calc(lambda x, y: x+y, 4, 5)



arr = []
for i in range(1, 21):
    if (i%2 == 0):
        arr.append(i)
print(arr)



arr1 = [i for i in range(1, 21) if i%2 == 0]
list1 = [(i,i) for i in range(1, 21) if i%2 == 0]
print(arr1)
print(list1)



def f(x):
    return x**3
list2 = [f(i) for i in range(1, 21) if i%2 == 0]
print(list2)

def f(x):
    return x**3
list3 = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
print(list3)


list4 = []
for i in range(list4):
    list4.append(int(input()))
print(list4)