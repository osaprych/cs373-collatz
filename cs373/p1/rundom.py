f = open('myfile','w')
import random

for w in range(1, 1005) :
	f.write(str(random.randint(1,1000000)))
	f.write(" ")
	f.write(str(random.randint(2,1000000)))
	f.write("\n")
