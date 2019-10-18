list1=[11,8,23,7,25,15]
list2=[6,33,50,31,45,46,78,16,34,21]
new_list=[]
alt_list=[]
li=[]
li1=[]
print(list1)
for i in range(len(list1)):
    a=2*list1[i]
    li.append(a)
    b=3*list1[i]
    li1.append(b)
print(li)
for i in range(len(list1)):
    for j in range(len(list2)):
        if li[i]==list2[j]:
            new_list.append(list1[i])
        if li1[i]==list2[j]:
            alt_list.append(list1[i])
print(new_list)
print(alt_list)
dic={}

for i in range(len(new_list)):
    for j in range(len(new_list)):
        if new_list[i]<new_list[j]:
            temp=new_list[i]
            new_list[i]=new_list[j]
            new_list[j]=temp
for i in range(len(alt_list)):
    for j in range(len(alt_list)):
        if alt_list[i]<alt_list[j]:
            temp=alt_list[i]
            alt_list[i]=alt_list[j]
            alt_list[j]=temp


print(new_list)
print(alt_list)            
dic['first']=new_list
dic['second']=alt_list
print(dic)
        
