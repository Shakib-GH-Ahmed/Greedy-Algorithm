x=open("input2.txt","r")
y=open("output2.txt","w")

line1=x.readline().split()
line1=[int(i) for i in line1]
new=[[] for j in range(line1[1])]
lst=[]

for i in range(line1[0]):
    l=x.readline().split(" ")
    l=[int(x) for x in l]
    lst.append(l)

lst.sort(key=lambda x:x[1])

count=0
for i in range(len(lst)):
  for j in range(len(new)):
    if new[j] == []:
      new[j].append(lst[i])
      count+=1
      break
    else:
      if new[j][0][1] <= lst[i][0]:
        new[j].append(lst[i])
        count+=1
        break

y.write(f"{count}")


#creating a new list taking the length using index-1 form line1
#lst takes the input values and store the sort values
#Taking a count variable for how many list that's appending to the new list and for the output also
#Inside the loop, if it's a empty list we add any of them in the new list.
#breaking the loop to go back the first loop to increase the value of i and iterate again
#At last, we just shows the count value as the output.