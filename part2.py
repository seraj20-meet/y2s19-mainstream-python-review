# Part 2 of the Python Review lab.

def encode(x, y):
	if y<250 and y>1 and 500<x and x<1000:
	 	return y*x
	else:
	 	pass
	 	print ("invalid input: outside range")
	 


def decode(coded_message):
	for y in range(2,250):
		for x in range(501,1000):
			if x*y == coded_message:
				return x,y


print(decode(1200))