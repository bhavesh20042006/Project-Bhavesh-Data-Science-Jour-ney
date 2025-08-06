# variables are used to store information in form of containers
name = input("what is your name?")
print(name)

name = "urvashi"
print(name)


name = "ansh"
print(name)
#these lines of code shows that variables can be varied


name = input("what is your name?")
length = len(name)
print("length of name is" ,length)
#len function is used to calculate the length of strings



'''We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice.
 Write 3 lines of code to switch the contents of the variables.'''
glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
print(glass1) 
print(glass2)