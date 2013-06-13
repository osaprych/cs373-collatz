f = open('myfile','w')
import random

for w in range(1, 10) :
	f.write(str(random.randint(1,100)))
	f.write(" ")
	f.write(str(random.randint(1,100)))
	f.write("\n")
