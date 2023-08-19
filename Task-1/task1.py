x=open("input1.txt","r")
y=open("output1.txt","w")

line1=int(x.readline().strip())
lst=[]
new=[]
for i in range(line1):
    l=x.readline().split(" ")
    l=[int(x) for x in l]
    lst.append(l)
    
lst.sort(key=lambda x:x[1])
new.append(lst[0])
j=0

for i in range(1,len(lst)):
    if new[j][1] <= lst[i][0]:
        new.append(lst[i])
        j+=1

y.write(f"{len(new)}\n")

for i in range(len(new)):
    if i==len(new)-1:
        y.write(f"{new[i][0]} {new[i][1]}")
    else:
        y.write(f"{new[i][0]} {new[i][1]}\n")

y.close()


#taken 2 empty lists
    #IN new, only append the first value initially
#sort the lst according to ending time interval
#run a for loop and iterate from 1 to length of the lst
#Inside the loop, it gives a condition that-
    #append the value if end value of new <= start value of lst
    
#Lastly, we print the new list in the output along with the count 'j'