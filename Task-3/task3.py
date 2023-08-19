x = open('input3.txt','r')
y = open('output3.txt','w')
line1 = x.readline()
line1 = list(map(int,line1.split()))
no_people = line1[0]
queries = line1[1]
arr = [1]* (no_people+1)
par = [None]* (no_people+1)

def find(r):
    if par[r] == r:
        return r
    return find(par[r])
for i in range(0,no_people+1):
    par[i] = i

for i in range(queries):
    line1 = x.readline()
    line1 = list(map(int,line1.split()))
    friend1 = line1[0]
    friend2 = line1[1]
    val1 = find(friend1)
    val2 = find(friend2)
    if val1 != val2:
        par[val2] = val1
        arr[val1] += arr[val2]
    if i!= queries-1:
        y.write(f"{arr[val1]}\n")
    else:
        y.write(f"{arr[val1]}")

y.close()

#arr: Initializes a list called arr with all elements set to 1. 
    # This list will be used to keep track of the size of each group of connected people.
#par = [None] * (no_people + 1): Initializes a list called par with None values.
    #This list will be used to represent the parent of each person in the group.
#function find that takes a person r as an argument and recursively finds their ultimate parent in the group.
#If par[r] is equal to r (i.e., r is its own parent), it returns r.
#Otherwise, it recursively calls the function until it reaches the ultimate parent.
