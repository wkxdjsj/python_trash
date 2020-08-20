#print hello world
def printHelloWorld():
	print("Hello World!")
#add 2 numbers
def addition(a, b):
	c = a+b
	return c

a = addition(10,3)
b = addition(4,6)

if (a < b):
	print("a < b")
else:
	printHelloWorld()