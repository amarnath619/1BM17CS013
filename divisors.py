n=int(input("Enter the number"))
divisors=[]
for i in range(1,n+1):
    if n%i==0:
        divisors.append(i)

print("The list of divisors are: ")
for j in divisors:
    print(j,end=" ")
print("\n")    
