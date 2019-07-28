# Part 1 of the Python Review lab.

def hello_world():
	print("hello world")

def greet_by_name(name):
	print("hello"+ name)

def encode(x):
	y =(x * 3953531)
	return y



def decode(y):
	x= y/3953531
	print (x)
	

hello_world()
	
	
greet_by_name(" seejo")
encode(5)

print(decode(encode(3)))
