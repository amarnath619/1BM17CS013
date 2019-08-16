a=0
b=1
i=2
fibo=[a, b]
v=input("enter the number of fibonacci series")
while i < v:
    a, b = b, a+b
    fibo.append(b)
    i=i+1
print fibo
