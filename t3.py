infile=open('names.txt','r')
line=[0]*4
line[0]=infile.readline()
line[1]=infile.readline()
line[2]=infile.readline()
line[3]=infile.readline()

for i in range(4):
    line[i]=line[i].rstrip('\n')
    firstname=line[i].split(' ')[0]
    lastname=line[i].split(' ')[1]
    print('Good evening Dr.'+lastname+" would you mind if I call you "+firstname+" ?")


